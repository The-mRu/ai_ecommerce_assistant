import json

from openai import OpenAI
from dotenv import load_dotenv
import os

from database.mongodb import load_conversation, save_message
from services.tools import (
    recommend_products_tool,
    search_products_tool,
    compare_products_tool,
    summarize_reviews_tool
)

from services.prompts import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# =========================
# TOOL DEFINITIONS
# =========================

tools = [

    {
        "type": "function",

        "name": "search_products_tool",

        "description": """
        Search products from e-commerce database.

        Use when user:
        - searches products
        - asks for gaming phones
        - wants recommendations
        - asks available products
        """,

        "parameters": {

            "type": "object",

            "properties": {

                "query": {
                    "type": "string"
                }
            },

            "required": ["query"]
        }
    },

    {
        "type": "function",

        "name": "compare_products_tool",

        "description": """
        Compare multiple products using database information and reviews.

        Use when user:
        - compares products
        - asks which is better
        - asks differences between products
        - mentions multiple products
        """,

        "parameters": {

            "type": "object",

            "properties": {

                "products": {

                    "type": "array",

                    "items": {
                        "type": "string"
                    }
                }
            },

            "required": ["products"]
        }
    }
]





# =========================
# INTENT EXTRACTION
# =========================

def extract_user_intent(message):

    extraction_prompt = f"""
    Extract structured shopping intent.

    Return ONLY valid JSON.
    Do not explain anything.
    Do not add markdown.
    Do not add extra text.

    Possible intents:
    - search_products
    - compare_products
    - recommend_products
    - normal_chat

    Possible fields:
    - category
    - max_price
    - products

    Examples:

    User:
    best gaming beast under 700

    Output:
    {{
        "intent": "recommend_products",
        "category": "gaming",
        "max_price": 700
    }}

    User message:
    {message}
    """

    response = client.responses.create(

        model="gpt-5-mini",

        input=extraction_prompt
    )

    return json.loads(response.output_text)

# =========================
# MAIN CHAT FUNCTION
# =========================

def ai_chat(user_id, message):
    
    conversation_history = load_conversation(user_id)
    
    # Save current user message
    save_message(user_id, "user", message)

    conversation_history.append({

        "role": "user",

        "content": message
    })
    
    # Scrub the data so it ONLY contains role and content
    clean_history = []
    for msg in conversation_history[-10:]:
        clean_history.append({
            "role": msg.get("role"),
            "content": msg.get("content")
        })
    
    response = client.responses.create(

        model="gpt-5-mini",

        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            *clean_history

            # {
            #     "role": "user",
            #     "content": message
            # }
        ],

        tools=tools
    )

    print(response)
    #Set a default reply in case no tools are called
    assistant_reply = response.output_text
    
    
    extracted_data = extract_user_intent(message)
    print("EXTRACTED DATA:")
    print(extracted_data)

    
    intent = extracted_data.get("intent")
    
    # =========================
    # RECOMMENDATION WORKFLOW
    # =========================

    if intent == "recommend_products":
    
        category = extracted_data.get("category")

        max_price = extracted_data.get("max_price")

        products = recommend_products_tool(

            category=category,

            max_price=max_price
        )

        final_prompt = f"""
    User request:
    {message}

    Matching products:
    {products}

    Recommend naturally.

    Rules:
    - Keep response short
    - Be conversational
    - Only use database products
    """

        final_response = client.responses.create(

        model="gpt-5-mini",

        input=final_prompt
    )

        assistant_reply = final_response.output_text

        save_message(
        user_id,
        "assistant",
        assistant_reply
    )

        return assistant_reply    



    # TOOL EXECUTION
    for item in response.output:

        if item.type == "function_call":

            tool_name = item.name

            arguments = json.loads(item.arguments)

            # =========================
            # SEARCH TOOL
            # =========================

            if tool_name == "search_products_tool":

                query = arguments.get("query")

                tool_result = search_products_tool(query)

                # return tool_result
                
                final_prompt = f"""
                User asked:
                {message}
                
                Products found:
                {tool_result}

                Reply naturally like a shopping assistant.

                Rules:
                - Keep response short
                - Be conversational
                - Recommend products naturally
                - Do not dump raw database text
                - Only recommend products available in database
                - Never recommend products not found in database
                - If product unavailable, politely say it is not available
                
                """

                final_response = client.responses.create(

                    model="gpt-5-mini",

                    input=final_prompt
                )

                assistant_reply = final_response.output_text
                # return assistant_reply
                break

            # =========================
            # COMPARE TOOL
            # =========================

            elif tool_name == "compare_products_tool":

                products = arguments.get("products")

                comparison = compare_products_tool(products)

                review_data = []

                for product in products:

                    reviews = summarize_reviews_tool(product)

                    review_data.append(
                        f"{product} Reviews:\n{reviews}"
                    )

                combined_reviews = "\n\n".join(review_data)

                final_prompt = f"""
                Compare these products using:

                Product Specs:
                {comparison}

                Customer Reviews:
                {combined_reviews}

                Give:
                - key differences
                - pros/cons
                - recommendation
                - short response
                
                Rules for response:
                - Keep the answer short, punchy, and beginner-friendly.
                - Max 2-3 sentences per product or a very brief bulleted breakdown.
                - No introductory phrases (e.g., do NOT say "Here is the comparison...").
                - Get straight to the comparison data.
                """

                final_response = client.responses.create(

                    model="gpt-5-mini",

                    input=final_prompt
                )

                assistant_reply = final_response.output_text
                # return assistant_reply
                break
    
    # SINGLE EXIT POINT
    # This guarantees every response is saved, whether it came from a tool or general chat
    save_message(user_id, "assistant", assistant_reply)
    return assistant_reply
    












# def testing(message):
#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a helpful assistant of The_mRu shop, an e-commerce store. You help customers with their queries and provide information about products, orders, and general assistance."
#             },
#             {
#                 "role": "user",
#                 "content": message
#             }
#         ]
#     )
#     return response.choices[0].message.content


