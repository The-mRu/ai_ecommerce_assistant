from database.mongodb import orders_collection
from datetime import datetime, timedelta

orders = [
    {
        "user": "rayhan",
        "products": ["iPhone 15", "AirPods Pro 2"],
        "total_price": 1248,
        "status": "Delivered",
        "order_date": datetime.now() - timedelta(days=5)
    },
    {
        "user": "rafi",
        "products": ["MacBook Pro M3", "Sony WH-1000XM5"],
        "total_price": 1948,
        "status": "Shipped",
        "order_date": datetime.now() - timedelta(days=2)
    },
    {
        "user": "mamun",
        "products": ["Lenovo Legion Pro 5i"],
        "total_price": 1399,
        "status": "Pending",
        "order_date": datetime.now()
    },
    {
        "user": "rayhan",
        "products": ["Dell XPS 15"],
        "total_price": 1499,
        "status": "Cancelled",
        "order_date": datetime.now() - timedelta(days=10)
    }
]

orders_collection.delete_many({})
orders_collection.insert_many(orders)

print(f"Successfully inserted {len(orders)} orders!")