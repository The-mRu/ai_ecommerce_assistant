from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

db = client["ai_ecommerce_assistant"]

# Collections (like tables in SQL)
users_collection = db["users"]

products_collection = db["products"]

reviews_collection = db["reviews"]

orders_collection = db["orders"]

chat_history_collection = db["chat_history"]




# =========================
# PRODUCTS
# =========================

def get_all_products():

    return list(products_collection.find({}, {"_id": 0}))


def get_product_by_name(name):

    return products_collection.find_one(
        {
            "name": {
                "$regex": name,
                "$options": "i"
            }
        },
        {
            "_id": 0
        }
    )


def search_products(query):

    query = query.lower().strip()

    # Simple normalization
    replacements = {

        "phones": "phone",
        "mobiles": "smartphone",
        "mobile": "smartphone",
        "cell phone": "smartphone",

        "gaming phones": "gaming",
        "gaming mobile": "gaming",
        "gaming smartphone": "gaming",

        "budget phone": "budget",
        "cheap phone": "budget"
    }

    for old, new in replacements.items():

        query = query.replace(old, new)

    return list(

        products_collection.find(

            {
                "$or": [

                    {
                        "name": {
                            "$regex": query,
                            "$options": "i"
                        }
                    },

                    {
                        "brand": {
                            "$regex": query,
                            "$options": "i"
                        }
                    },

                    {
                        "category": {
                            "$regex": query,
                            "$options": "i"
                        }
                    },

                    {
                        "sub_category": {
                            "$regex": query,
                            "$options": "i"
                        }
                    },

                    {
                        "tags": {
                            "$regex": query,
                            "$options": "i"
                        }
                    }
                ]
            },

            {
                "_id": 0
            }
        )
    )


# =========================
# REVIEWS
# =========================

def get_reviews_by_product(product_name):

    return list(

        reviews_collection.find(

            {
                "product_name": {
                    "$regex": product_name,
                    "$options": "i"
                }
            },

            {
                "_id": 0
            }

        ).sort("created_at", -1)
    )
    


# =========================
# CHAT HISTORY
# =========================

def save_message(user_id, role, content):

    chat_history_collection.insert_one({

        "user_id": user_id,

        "role": role,

        "content": content
    })


def load_conversation(user_id, limit=10):

    messages = list(

        chat_history_collection.find(

            {
                "user_id": user_id
            },

            {
                "_id": 0
            }

        ).sort("_id", -1).limit(limit)
    )

    messages.reverse()

    return messages
    
    
    
    
# =========================
# RECOMMEND PRODUCTS
# =========================

def recommend_products(category=None, max_price=None):
    
    if category:
        category = category.lower()

        category_mapping = {

        "mobile": "smartphone",
        "phone": "smartphone",
        "android": "smartphone",
        "gaming": "gaming"
    }

    category = category_mapping.get(
        category,
        category
    )

    query = {}

    # CATEGORY FILTER
    if category:

        query["$or"] = [

            {
                "category": {
                    "$regex": category,
                    "$options": "i"
                }
            },

            {
                "sub_category": {
                    "$regex": category,
                    "$options": "i"
                }
            },

            {
                "tags": {
                    "$regex": category,
                    "$options": "i"
                }
            }
        ]

    # PRICE FILTER
    if max_price:

        query["price"] = {
            "$lte": max_price
        }
        
    print("FINAL QUERY:")
    print(query)


    products = list(
        
        products_collection.find(

            query,

            {
                "_id": 0
            }

        ).sort("rating", -1)
    )
    print("FOUND PRODUCTS:")
    print(products)

    return products