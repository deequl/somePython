
#_REVERSED_FUNCTION____________________

nums = [3,67,99, 44]
reversed_numbers= list(reversed(nums))
print(reversed_numbers)

reversed_str= "hello!"[::-1] #sliced method
print(reversed_str)

reversed_str = ''.join(list(reversed("hello!")))
print(reversed_str)

for x in reversed(range(0,10)):
    print(x)