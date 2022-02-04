


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#
# ask for user input

u = input("Please choose one: 'Rock','Paper', 'Scissors','?".lower())
print("USER CHOSE:", u)
print("Rock, Paper, Scissors, Shoot!")
     




#Validations
#look up go too method, not required. have it fail gracefully. if statement if the input is not rock... print user input is wrong. then exit()
#make user input all lower cased. and in if statement do everything else lower case. 
if u.lower() != "Rock".lower():
    print("Incorrect user input, try again")
elif u.lower() != "Paper".lower():
    print("Incorrect user input, try again")
elif u.lower() != "Scissors".lower(): 
    print("Incorrect user input, try again")


#computer choice
# Computers choice is defined by variable c
import random
options = ["Rock", "Paper", "Scissors"]
c = random.choice(options)
print("Computer Chose:",c)


#Determine the winner
if u.lower() == c.lower() :
    print("You both played",c,"Its a tie!")
elif u.lower()  == "Rock".lower() :
    if c.lower()  == "Paper".lower() :
        print("Paper beats rock, you lose.")
    else:
        print("Rock beats scissors, you win!")
elif u.lower()  == "Paper".lower() :
    if c.lower()  == "Scissors".lower() :
        print("Scissors beats paper, you lose.")
    else:
        print("Paper beats rock, you win")
elif u.lower()  == "Scissors".lower() :
    if c.lower()  == "Rock".lower() :
        print("Rock beats scissors, you lose.")
    else:
        print("Scissors beats paper, you win!")






#final results