import random
choices = ["Rock", "Paper", "Scissor"]
userChoice = input("Choose one in (Rock, Paper and Scissor: ").capitalize()
print(f"You choose {userChoice}")
comChoice = choices[random.randrange(0,2)]
print(f"Computer choose {comChoice}")

if userChoice == comChoice:
    print("Its Draw, Try Again")
    
    #when user choose Rock
elif (userChoice == "Rock" and comChoice == "Paper"):
    print("Computer won the game")
elif (userChoice == "Rock" and comChoice == "Scissor"):
    print("You Won the game")
    
    #when user chhoose Paper
elif(userChoice == "Paper" and comChoice == "Rock"):
    print("You Won the game")
elif(userChoice == "Paper" and comChoice == "Scissor"):
    print("Computer Wom the game")
    
#whem user choose Scissor
elif(userChoice == "Scissor" and comChoice == "Rock"):
    print("Computer Won the game")
elif(userChoice == "Scissor" and comrChoice == "Paper"):
    print("You Won the game")
