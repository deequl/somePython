def colorize(text, color):
    colors = ("cyan", "yellow", "blue")
    if type(text) is not str:
        raise TypeError("Text must be string")
    if color not in colors:
        raise Exception("This color is not avaliable")
    print(f"Printed '{text}' in {color}")
colorize("Hi, there!", "blue")
#colorize(89, "blue")
#colorize("Hi, there!", "red")


try:
    foobar
except NameError as err:
    print(err)


d = {"name": "Rick"}
def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None
print(get(d, "name"))
print(get(d, "city"))


while True:
    try:
        num = int(input("Please enter a number: "))
    except ValueError as err:
        print("That's not a number!")
        print(err)
    else:
        print("Perfect. It's a number")
        break
    finally:
        print("Runs no matter what!")


def divide(dividend, divisor):
    try:
        result = dividend/divisor
    except (ZeroDivisionError, BufferError) as err:
        print("don't divide by 0")
        print(err)
    except TypeError:
        print ("a and b have to be ints or floats ")
    else:
        print(f"{dividend} divided by {divisor} is {result}")
divide(10, 5)


    # divide(4,2)  2
    # divide([],"1")  "Please provide two integers or floats"
    # divide(1,0)  "Please do not divide by zero"
def divide2(num1, num2):
    try:
        result = num1 / num2
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    else:
        return result