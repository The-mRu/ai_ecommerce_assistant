from database.mongodb import products_collection

products = [

    {
        "name": "iPhone 15",
        "brand": "Apple",

        "category": "Smartphone",
        "sub_category": "Flagship",

        "price": 999,
        "stock": 20,

        "battery": "3349mAh",
        "camera": "48MP",
        "display": "6.1-inch OLED",
        "processor": "A16 Bionic",
        "ram": "6GB",
        "storage": "128GB",

        "gaming": "Good",
        "rating": 4.7,

        "tags": [
            "ios",
            "flagship",
            "camera"
        ],

        "description": "Latest Apple smartphone with excellent camera."
    },

    {
        "name": "Samsung S24",
        "brand": "Samsung",

        "category": "Smartphone",
        "sub_category": "Flagship",

        "price": 899,
        "stock": 15,

        "battery": "4000mAh",
        "camera": "50MP",
        "display": "6.2-inch AMOLED",
        "processor": "Snapdragon 8 Gen 3",
        "ram": "8GB",
        "storage": "256GB",

        "gaming": "Very Good",
        "rating": 4.8,

        "tags": [
            "android",
            "flagship",
            "gaming"
        ],

        "description": "Premium Samsung flagship with strong battery."
    },

    {
        "name": "Asus ROG Phone 8",
        "brand": "Asus",

        "category": "Smartphone",
        "sub_category": "Gaming Phone",

        "price": 1199,
        "stock": 10,

        "battery": "5500mAh",
        "camera": "50MP",
        "display": "6.78-inch AMOLED",
        "processor": "Snapdragon 8 Gen 3",
        "ram": "16GB",
        "storage": "512GB",

        "gaming": "Excellent",
        "rating": 4.9,

        "tags": [
            "gaming",
            "high-performance",
            "android"
        ],

        "description": "High-end gaming smartphone with advanced cooling."
    },

    {
        "name": "Google Pixel 8",
        "brand": "Google",

        "category": "Smartphone",
        "sub_category": "Camera Phone",

        "price": 799,
        "stock": 12,

        "battery": "4575mAh",
        "camera": "50MP",
        "display": "6.2-inch OLED",
        "processor": "Google Tensor G3",
        "ram": "8GB",
        "storage": "128GB",

        "gaming": "Good",
        "rating": 4.6,

        "tags": [
            "camera",
            "android",
            "ai"
        ],

        "description": "Google AI-powered smartphone with excellent camera."
    },

    {
        "name": "Poco F6 Pro",
        "brand": "Xiaomi",

        "category": "Smartphone",
        "sub_category": "Gaming Phone",

        "price": 599,
        "stock": 30,

        "battery": "5000mAh",
        "camera": "50MP",
        "display": "6.67-inch AMOLED",
        "processor": "Snapdragon 8 Gen 2",
        "ram": "12GB",
        "storage": "256GB",

        "gaming": "Excellent",
        "rating": 4.5,

        "tags": [
            "budget",
            "gaming",
            "android"
        ],

        "description": "Affordable gaming phone with flagship performance."
    }
]

products_collection.delete_many({})

products_collection.insert_many(products)

print("Products inserted successfully")