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


def check_guess (guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input ():
    check_guess(guess)
    while True:
        guess = input('Guess a Letter')
        if guess.isalpha() and len(guess) == 1:
          check_guess(guess)
          break
    
    else: 
        print('Invalid letter. Please, enter a single alphabetical character.')







