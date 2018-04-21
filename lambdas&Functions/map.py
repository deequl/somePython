
#_MAP_FUNCTION_____________________________

nums = [2,4,6,8,10]
doubles = list(map(lambda x: x*2 ,nums))
print(doubles)

people = ["Darcy", "Christina", "Dana", "Annabel"]
peeps = list(map(lambda name: name.upper(), people))
print(peeps)

names = [
    {'first':'Darcy', 'last': 'Steele'},
    {'first':'Rusty', 'last': 'Dana'}
]
first_name = list(map(lambda x: x['first'], names))
print(first_name)

def decrement_list(numbersList):
    return list(map(lambda n: n-1, numbersList))