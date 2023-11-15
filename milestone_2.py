import random

favourite_fruits = ['Banana', 'Apple', 'Pear', 'Raspberry', 'Orange']

def valid_input(func):
    def wrapper():
        guess = input('Input a single letter: ')

        if len(guess) == 1 and guess.isalpha():
            print('Great guess!')
            func(guess)
        else:
            print('Oops! That is not a valid input')

    return wrapper


@valid_input
def main_function(guess):
    word = random.choice(favourite_fruits)
    # Add your main function logic here, using the guessed letter if needed
    print(f'The randomly chosen fruit is: {word}')

if __name__ == "__main__":
    main_function()
