import random

print("Welcome to Rock, Paper, Scissors!")


player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
computer_choice = random.choice(["rock", "paper", "scissors"])

print(f"you chose: {player_choice}")
print(f"computer chose: {computer_choice}")

if player_choice == computer_choice:
    print("Guys it's a tie!")
elif player_choice == "rock":
    if computer_choice == "scissors":
        print("you win!")
    else:
        print("you lose!")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("you win")
    else:
        print("you lose!")
elif player_choice == "scissors":
    if computer_choice == "paper":
        print("you win")
    else:
        print("you lose!")
else:
    print("invalid choice and look well")