import json

fp = "Learning/user_data.json"

with open(fp, 'r') as f:
    user_name = json.load(f)

print(f"Welcome back, {user_name}!")