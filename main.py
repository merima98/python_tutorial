print("Hello, World!")


users=[
    {"id":1, "name":"John"},
    {"id":2, "name":"Jane"},
    {"id":3, "name":"Doe"}
]
results=[]

def get_name_users(users):
    for user in users:
        results.append(user["name"])
    return results

print(get_name_users(users))