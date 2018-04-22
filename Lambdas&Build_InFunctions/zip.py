
#_ZIP_FUNCTION_____________________________

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10, 11, 12]
z = zip(nums1, nums2)
zlist = list(z) #[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
zdict = dict(z) #{1: 6, 2: 7, 3: 8, 4: 9, 5: 10} 

#unpacked *
five_by_two = [(0, 1), (2, 3), (4, 5), (6, 4), (8, 5)]
list(zip(*five_by_two)) # [(0, 2, 4, 6, 8), (1, 3, 5, 4, 5)]

midterms = [80,91,78]
finals = [98,89,53]
students = ["Crhi", "Lum", "Wicy"]
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}
print (final_grades) #{'Crhi': 98, 'Lum': 91, 'Wicy': 78}

midterms = [80,91,78]
finals = [98,89,53]
students = ["Crhi", "Lum", "Wicy"]
grades = zip(
    students,
    map(
        lambda pair: ((pair[0]+pair[1])/2),
        zip(midterms, finals)
    )
)
print(dict(grades)) #{'Crhi': 98, 'Lum': 91, 'Wicy': 78}

#interleave('aaa', 'zzz') -> #'azazaz'
def interleave(str1, str2):
    return "".join(["".join(pr) for pr in zip(str1, str2)])