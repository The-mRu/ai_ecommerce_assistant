# from database.mongodb import search_products

# products = search_products("gaming")

# print(products)

# from services.tools import (
#     search_products_tool,
#     compare_products_tool
# )

# print(search_products_tool("gaming"))

# print("----------------")

# print(
#     compare_products_tool(
#         ["iPhone 15", "Samsung S24"]
#     )
# )


# from services.ai_service import extract_user_intent
# result = extract_user_intent(
#     "best gaming beast under 700"
# )

# print(result)


from database.mongodb import recommend_products

products = recommend_products(

    category="gaming",

    max_price=700
)

print(products)