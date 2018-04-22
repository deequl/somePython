import math

#_ABS_FUNCTION_____________________________

abs(-5) #5
#math.fabs(-4) #4.0

#_SUM_FUNCTION_____________________________

sum([1,2,3]) #6
sum([1,2,3], 10) #16

#_ROUND_FUNCTION___________________________

round(10.2) #10
round(1.2121, 2) #1.21


def max_magnitude(numbers):
    positive_numbers = [abs(num) for num in numbers]
    return max(positive_numbers)

def sum_even_values(*args):
    return sum((num for num in args if num%2==0))

def sum_floats(*args):
    return sum((fnum for fnum in args if type(fnum)==float))
    #return sum((fnum for fnum in args if type(fnum).__name__=='float'))