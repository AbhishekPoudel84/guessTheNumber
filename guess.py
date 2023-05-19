import random
import math
 #taking inputs
lower = int(input("Enter Lower bound:-"))

upper = int(input("Enter Upper Bound:- "))


#generating random number between upper and lower
x = random.randint(lower, upper)
print("\n\tYou have only ",
        round(math.log(upper-lower+1,2)),
        "chances to guess the interger!\n")

#initializling the number of guesses
count = 0        

while count< math.log(upper-lower+1,2):
    count += 1


    #taking guessing number as input
    guess = int(input("Guess a number:-"))

#testing
    if x == guess :
        print("Congratulation you did it in", count, "try")
    #loop will break
        break
    elif x > guess:
        print("You guessed too small !")
    elif x < guess:
        print("You guessed too high !")

#if user cant guess in give chances
if count >= math.log(upper-lower+1,2):
    print("\n The number is %d" % x) 
    print("\n Better Luck Next Time!")  


