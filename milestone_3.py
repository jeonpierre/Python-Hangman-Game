
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
          check_guess(guess)break
    
    else: 
        print('Thats an Invalid letter. Please, enter a single alphabetical character.')








