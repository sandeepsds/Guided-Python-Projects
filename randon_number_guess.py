import random

selected_number = random.randint(1, 100)

user_input = 0
guess_count = 0

print("You get 6 guesses!")

while not user_input == selected_number:
    user_input = int(input("Enter a number: "))

    if user_input > selected_number:
        print("Too High!")
    elif user_input < selected_number:
        print("Too Low!")
    else:
        print("That's Right!")
    if guess_count >= 5:
        print("You're out of guesses! Try again.")
        break
    guess_count += 1

