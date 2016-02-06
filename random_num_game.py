def randomnumgame(high):
    import random

    answer = random.randint(1,high)

    guess = 0
    guesses = 0
    remain = 5

    if high <=5:
        print "\n\nReally? You can't even make it larger than between 1 and 5? \nGAME OVER, SUCKA!"
    else:
        high = str(high)
        while answer != guess and guesses <5:

            # Print number of remaining guesses and prompt to user
            print "You have", remain-guesses, "guess remaining.\n"
            guess = int(raw_input("I'm thinking of a number between 1 and " + high + ". Guess! (int only please):\n"))


            # Conditionals to evaluate guess
            if answer == guess:
                print "Attempt", guesses+1, "- Wow! That is right. My number was", guess
            elif answer > guess:
                print "No,", guess, "is too low!"
                guesses +=1
            elif answer < guess:
                print "Attempt", guesses+1, "- No,", guess, "is too high!"
                guesses +=1
            else:
                print "ERROR: Hum, something went wrong"

        if guesses == 5:
            print "\n\nNo. It was", answer

upperrange = int(raw_input("What do you want the upper limit to be?"))
randomnumgame(upperrange)