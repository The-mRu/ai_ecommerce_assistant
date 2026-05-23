from database.mongodb import users_collection

users = [
    {"username": "rayhan", "email": "rayhan@gmail.com", "role": "customer"},
    {"username": "admin", "email": "admin@gmail.com", "role": "admin"},
    {"username": "mamum", "email": "mamum@example.com", "role": "customer"},
    {"username": "rafi", "email": "rafi@example.com", "role": "customer"},
    {"username": "sayeem", "email": "sayeem@example.com", "role": "developer"}
]

users_collection.delete_many({})
users_collection.insert_many(users)

print(f"Successfully inserted {len(users)} users!")