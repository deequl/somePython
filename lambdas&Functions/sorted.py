
#_SORTED_FUNCTION_______________________

numbers = [6,1,8,2]
#admits tuples too numbers = (6,1,18,2)
sorted(numbers) #[1,2,6,8]
sorted(numbers, reverse=True) #[8,6,2,1]
print(numbers) #[6,1,8,2]

users = [
    {"username": "samu", "tweets": ["I love cake", "I love pie"]},
    {"username": "bob", "tweets": [], "color": "blue"},
    {"username": "andre", "tweets": [], "city": "Barcelona", "num": 10},
    {"username": "palom", "tweets": ["I love pie"]}
]
#print(sorted(users, key=len))
sorted_inactive_users = sorted(users, key=lambda user: len(user["tweets"]))
print(sorted_inactive_users)