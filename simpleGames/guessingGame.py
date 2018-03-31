import random
lower = 1
higher = 10
number_picked = random.randint(lower,higher)
while True :
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > number_picked :
        print("Too high, try again!")
    elif guess < number_picked :
        print("Too low, try again!")
    elif guess == number_picked :
        print("You guessed it!")
        again = input("Do you want to keep playing? (y/n) ")
        print("=============================")
        if(again=="y"):
            number_picked = random.randint(lower,higher)
            guess = None
        elif(again=="n"):
            print("Ok, bye.")
            break
