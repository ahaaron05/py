import json

user_name = input("What is your name: ")

fp = "Learning/user_data.json"
with open(fp, 'w') as f:
    json.dump(user_name, f)