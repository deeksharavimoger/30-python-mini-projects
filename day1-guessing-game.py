import random

secret = random.randint(1,50)
chances = 5

print("u have 5 chances to guess(1-50)")

while chances > 0:
    guess = int(input("enter guess: "))

    if guess == secret:
        print("you win🎉😎")
        break
    elif guess < secret:
        print("too low↘️")
    else:
        print("too high↗️")

    chances -= 1
    print("remaining chances:",chances)

if chances == 0:
    print("game over🥹")
    print("the number was :",secret)
