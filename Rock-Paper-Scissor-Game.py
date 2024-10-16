import random
user_Choice = input("Choose Rock, Paper or Scissors: ").capitalize()
computer_Choice = random.choice(["Rock", "Paper", "Scissors"])
match computer_Choice:
  case "Rock":
    print("Computer Choose Rock")
    match user_Choice:
      case "Rock":
        print("Its tie! Try Again")
      case "Paper":
        print("You Won")
      case "Scissors":
        print("You Lost")
  case "Paper":
    print("Computer Choose Paper")
    match user_Choice:
      case "Rock":
        print("You Lost")
      case "Paper":
        print("Its tie! Try Again")
      case "Scissors":
        print("You Won")
  case "Scissors":
    print("Computer Choose Scissors")
    match user_Choice:
      case "Rock":
        print("You Won")
      case "Paper":
        print("You Lost")
      case "Scissors":
        print("Its tie! Try Again")
