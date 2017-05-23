"""A number-guessing game."""

import random

user_name = raw_input("Welcome! What should I call you? ")
print "Hey %s!" % (user_name)

random_num = random.randint(0, 100)
num_guesses = 1


while True:
    try:
        user_num = int(raw_input("Guess a number between 0 and 100! "))
        if user_num != random_num:
            if user_num < random_num:
                print "Your guess is too low! Try again! "
            else:
                print "Your guess is too high! Try again! "
            num_guesses += 1
        else:
            print "Congratulations, %s! You got it right in %d guesses! " % (user_name, num_guesses)
            break
    except ValueError:
        print "Oops! Invalid number! Try again! "
