# HL component 3 - compares user guess with secret number

# To Do
# Set up number of guesses
# Count # number of gusses
# if user runs out of guesses, print 'you lose'
# if user guesses the scecret number within the number of guesses print 'well done'

SECRET = 7
GUESSES_ALLOWED = 4

# initialise variables
guesses_left = GUESSES_ALLOWED
num_won = 0
guess = ""

# Start game
while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))  # replace this with function call in due count
    guesses_left -= 1

    # If user had guesses left...
    if guesses_left >= 1:

