git push 
import random
favourite_fruits = ['Bannana','Apple','Pear','Rasberry','Orange']
word_list = favourite_fruits

print(word_list)

Word = random.choice(favourite_fruits)
print(Word)

guess = input(str('Input a single letter'))

if len(guess) == 1 and guess.isalpha():
    print('great guess')
else:
    print('Oops! That is not a valid input')


