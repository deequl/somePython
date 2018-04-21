
#_MAX_MIN_FUNCTION______________________

nums = [3,67,99]
max_number= max(nums)
print(max_number)

min_number= min(nums)
print(min_number)

letters = 'Tom makez'
max_letter=max(letters)
print(max_letter) # 'z'

names = ['Arya', 'Samson', 'Daro', 'Tim', 'Ollivander']
longest_name = max(names, key=lambda n: len(n))
print(longest_name)

songs = [
    {'title': 'Focx', 'playcount': 1},
    {'title': 'YAND', 'playcount': 22},
    {'title': 'YMCA', 'playcount': 19},
    {'title': 'Tomy', 'playcount': 6}
]
minimum_playcount_title = min(songs, key=lambda n: n['playcount'])['title']
print(minimum_playcount_title)

def extremes(iter):
    return(min(iter), max(iter))