# This is a guess the number game

#This is for randint function to get a random number 
import random
#\' is an escape character to get apostrophe without terminating the string early 
print ('Hello! What\'s your name')
name = input()

#generates a random number 1-20 (including 1 and 20)
secretNumber = random.randint(1,20)
print ('Well, ' + name + ', I\'m thinking of a number between 1 and 20')

# Ask the player to guess 6 times
# the variable i is known locally, not just inside the loop 
for i in range (1,7):
    print('Take a guess')
    print('You have ' + str(7-i) + ' guesses remaining')

    # save user input to compare to secret number 
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    # guess == secretNumber 
    else:
        break

if guess == secretNumber:
    print('Yep, and you guessed the number in ' + str(i) + ' guesses. Nice work ' + name + '!')
else:
    print('Nope, and you ran out of guesses. The number I was thinking of was ' + str(secretNumber) +  '. Better luck next time!')
