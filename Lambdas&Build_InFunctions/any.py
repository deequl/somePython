
#_ALL_FUNCTION__________________________

people = ["Carch", "Chris", "Coshe", "Carmo"]
C_name= any([name[0]=='K' for name in people])
print(C_name) #False

people.append("Krsitof")
C_name= any([name[0]=='K' for name in people])
print(C_name) #True

numbers = [3,42,25,17]
even = any([num%2==0 for num in numbers])
print(even) #True