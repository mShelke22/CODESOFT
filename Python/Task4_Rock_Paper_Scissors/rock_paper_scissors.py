import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    print("\nRock Paper Scissors Game")
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)

    print("Your choice:", user_choice)
    print("Computer choice:", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You Win!")
        user_score += 1
    else:
        print("You Lose!")
        computer_score += 1

    print("Score -> You:", user_score, "Computer:", computer_score)

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        print("Game Over")
        break
