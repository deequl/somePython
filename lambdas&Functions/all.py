
#_ALL_FUNCTION__________________________

people = ["Carch", "Chris", "Coshe", "Carmo"]
C_name= all([name[0]=='C' for name in people])
print(C_name) #True

people.append("Krsitof")
C_name= all([name[0]=='C' for name in people])
print(C_name) #False

numbers = [2,60,26,18]
even = all([num%2==0 for num in numbers])
print(even) #True

elements = ['a', 'b', 'c']
is_all_strings = all([type(e).__name__=='str' for e in elements])
# all(type(e) == str for e in elements)
print(is_all_strings)