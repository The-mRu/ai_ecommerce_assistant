from database.mongodb import reviews_collection

reviews_collection.delete_many({})

reviews = [

    {
        "product_name": "iPhone 15",
        "user": "rayhan",
        "rating": 5,
        "review": "Excellent camera and smooth performance.",
        "created_at": "2026-05-20"
    },

    {
        "product_name": "iPhone 15",
        "user": "mamun",
        "rating": 4,
        "review": "Battery is decent but expensive.",
        "created_at": "2026-05-21"
    },

    {
        "product_name": "Samsung S24",
        "user": "rayhan",
        "rating": 5,
        "review": "Amazing display and gaming performance.",
        "created_at": "2026-05-18"
    },

    {
        "product_name": "Samsung S24",
        "user": "rafi",
        "rating": 4,
        "review": "Battery life is very good.",
        "created_at": "2026-05-22"
    },

    {
        "product_name": "Asus ROG Phone 8",
        "user": "gaming_king",
        "rating": 5,
        "review": "Best gaming phone with excellent cooling.",
        "created_at": "2026-05-19"
    },

    {
        "product_name": "Asus ROG Phone 8",
        "user": "sayeem",
        "rating": 4,
        "review": "Heavy phone but performance is insane.",
        "created_at": "2026-05-22"
    }
]

reviews_collection.insert_many(reviews)

print("Reviews inserted successfully")