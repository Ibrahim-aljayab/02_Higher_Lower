# HL component 7 _ Generates desired number of rounds...

rounds = int(input("How many rounds? "))    # check wiht integer checker in due course
rounds_played = 0

while rounds_played < rounds:
    print("Round {}".format(rounds_played+1))
    rounds_played += 1

print("You have gotten to the end of the game")