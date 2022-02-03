


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#
# ask for user input

u = input("Please choose one: 'Rock','Paper', 'Scissors','?".lower().title())
print("USER CHOSE:", u)
print("Rock, Paper, Scissors, Shoot!")
     




#Validations




#computer choice
# Computers choice is defined by variable c
import random
options = ["Rock", "Paper", "Scissors"]
c = random.choice(options)
print("Computer Chose:",c)


#Determine the winner
if u.lower().title() == c.lower().title() :
    print("You both played",c,"Its a tie!")
elif u.lower().title()  == "Rock".lower().title() :
    if c.lower().title()  == "Paper".lower().title() :
        print("Paper beats rock, you lose.")
    else:
        print("Rock beats scissors, you win!")
elif u.lower().title()  == "Paper".lower().title() :
    if c.lower().title()  == "Scissors".lower().title() :
        print("Scissors beats paper, you lose.")
    else:
        print("Paper beats rock, you win")
elif u.lower().title()  == "Scissors".lower().title() :
    if c.lower().title()  == "Rock".lower().title() :
        print("Rock beats scissors, you lose.")
    else:
        print("Scissors beats paper, you win!")






#final results