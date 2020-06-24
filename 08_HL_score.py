# HL component 8 - set up aore mechanics

# To Do
# Set up round and win counter
# update feedback statements


SECRET = 7
GUESSES_ALLOWED = 4
rounds = 3

num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = GUESSES_ALLOWED

    while guess != SECRET and guesses_left >= 1:

        guess = int(input("Guess: "))   # replace this with function call in due count
        guesses_left -= 1

        if guesses_left >= 1:

            if guess < SECRET:
                print("Too low, try a higher number.    Guesses left: {}".format(guess))