import random
print("-------------THE GAME---------------")
print("Welcome to 'rock' 'paper' 'scissors'")
print("------------------------------------")

player = input("Player choice: ")
computer = random.choice(["rock", "paper", "scissors"])

if player and computer :
    if(player=="rock" or player=="paper" or player=="scissors") :
        print(f"Computer choice: {computer}")
        print("------------------------------------")
        if player == "rock":
            if computer == "scissors" :
                print("You win!")
            elif computer == "paper" :
                print("You lose!")
            else :
                print("Draw")

        if player == "paper":
            if computer == "rock" :
                print("You win!")
            elif computer == "scissors" :
                print("You lose!")
            else :
                print("Draw")

        if player == "scissors":
            if computer == "paper" :
                print("You win!")
            elif computer == "rock" :
                print("You lose!")
            else :
                print("Draw")  
    else :
        print("Invalid move: Use 'rock' 'paper' or 'scissors'")      
else :
    print("Invalid move: Use 'rock' 'paper' or 'scissors'") 
print("====================================")