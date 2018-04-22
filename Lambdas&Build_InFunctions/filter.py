
#_FILTER_FUNCTION__________________________

nums = [1,2,3,4]
evens = list(filter(lambda n: n % 2 == 0, nums))
print(nums)

names = ["austin", "penny", "angel", "billy"]
a_names=list(filter(lambda n: n[0]=='a', names))
print(a_names)

users = [
    {"username": "samu", "tweets": ["I love cake", "I love pie"]},
    {"username": "bob", "tweets": []},
    {"username": "andre", "tweets": []},
    {"username": "palom", "tweets": ["I love pie"]}
]
inactive_users = list(
    map(lambda user: user["username"].upper(), 
        filter(lambda n: not n["tweets"], users)))
#LIST_Comprehension__
# [user["username".upper()] for user in users if not user["tweets"]]        
print(inactive_users)

def remove_negatives(numberList):
    return list(filter(lambda n: n>=0, numberList))

def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))