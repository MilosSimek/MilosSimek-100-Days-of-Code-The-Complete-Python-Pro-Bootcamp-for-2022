import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
random_number = random.randrange(1, 100)
print(random_number)

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")


def guess(number_of_attempts):
    """
    Guessing function requires number of guesses (int)
    """
    print(f"You have {number_of_attempts} attempts remaining to guess the number")
    guess_number = int(input("Make a guess: "))
    while guess_number != random_number and number_of_attempts != 0:
        if guess_number < random_number:
            print("Too low")
        else:
            print("Too high")
        number_of_attempts -= 1
        if number_of_attempts == 0:
            print("You've run out of guesses, you lose.")
        else:
            print(f"You have {number_of_attempts} attempts remaining to guess the number")
            guess_number = int(input("Make a guess: "))
    if guess_number == random_number:
        print(f"You got it! The answer was {random_number}")


if difficulty_level == 'easy':
    easy= 10
    guess(easy)
else:
    hard = 5
    guess(hard)
    
    
    


