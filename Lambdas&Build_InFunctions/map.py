
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

def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

#names = [{'first': 'Doo', 'last': 'Kanup'}, {'first': 'Marc', 'last': 'Jim'}]
#extract_full_name(names) # ['Doo Kanup', 'Marc Jim']
def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))