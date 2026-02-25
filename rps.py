import random

choices = ["rock","paper","scissors"]

user_score = 0
computer_score = 0

print("🎮 Rock Paper Scissors Game")
print("Type 'exit' to quit\n")

while True:
    user = input("Choose rock, paper, or scissors:").lower()

    if user == "exit":
        print("\nFinal Score 🏆")
        print("You:",user_score)
        print("Computer:",computer_score)
        print("Good game 👋")

    if user not in choices:
        print("Invalid choice ⚠️ Try again.\n")
        continue
    computer = random.choice(choices)
    print("Computer chose:",computer)

    if user == computer:
        print("it's a tie 🤝")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("you win this round 🥳")
        user_score += 1

    else:
        print("computer wins this round😎")

        computer_score += 1

    print(f"Score ➡️ You: {user_score} | Computer: {computer_score}\n ") 
    