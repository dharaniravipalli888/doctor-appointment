# models.py

# Schema for User
user_schema = {
    "username": {"type": "string", "unique": True, "required": True},
    "password": {"type": "string", "required": True}
}
