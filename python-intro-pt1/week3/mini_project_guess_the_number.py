# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# http://www.codeskulptor.org/#user43_htcW1Are2E_5.py

import simplegui
import random
import math


secret_number = 0
number_range = 100
guesses = 7
guesses_left = 7


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global number_range, secret_number, guesses, guesses_left
    guesses_left = guesses
    
    secret_number = random.randrange(0, number_range)
    print number_range, secret_number, guesses, guesses_left

    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global number_range, guesses, guesses_left
    number_range = 100
    guesses = 7
    guesses_left = 7
    new_game()

    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global number_range, guesses, guesses_left
    number_range = 1000
    guesses = 10
    guesses_left = 10
    new_game()

    
def input_guess(guess):
    global number_range, secret_number, guesses, guesses_left
    
    guesses_left -= 1
    
    # main game logic goes here	
    print "You've guessed " + str(guess)
    
    if guesses_left > 0:
        if int(guess) == secret_number:
            print "Congrats, you've guessed the secret number."
            print "A new game is starting now with your previous number range of 0 to " + str(number_range) +"."
            print "You'll have " + str(guesses) + " tries to guess the new number."
            new_game()
        elif int(guess) < secret_number:
            print "Pick higher!"
            print "Number of guesses left is " + str(guesses_left) + "."

        elif int(guess) > secret_number:
            print "Go lower!!"
            print "Number of guesses left is " + str(guesses_left) + "."

        else:
            print "ERROR"
                    
    else:
        if int(guess) == secret_number:
            print "Congrats, you've guessed the secret number."
            print "A new game is starting now with your previous number range of 0 to " + str(number_range) +"."
            print "You'll have " + str(guesses) + " tries to guess the new number."
            new_game()
        else:
            print "You didn't guess the number and ran out of guesses. Game Over!"
            print "A new game is starting now with your previous number range of 0 to " + str(number_range) +"."
            print "You'll have " + str(guesses) + " tries to guess the new number."
            new_game()

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess:", input_guess, 200)


# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
