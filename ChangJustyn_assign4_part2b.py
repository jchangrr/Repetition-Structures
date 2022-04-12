"""
Assignment #4, Problem #2b
Justyn Chang
"""

#ask for valid input for number of sticks
sticks = int(input("How many sticks (10-100)? "))
while True:
    if sticks > 100:
        print("Sorry, that's too many sticks. Try again")
        sticks = int(input("How many sticks (10-100)? "))
    elif sticks < 10:
        print("Sorry, that's too few sticks. Try again")
        sticks = int(input("How many sticks (10-100)? "))
    else:
        break
print("Great Let's play ...")
print()
turn = 0

while True:
    #determine who's turn it is
    turn += 1
    if turn % 2 == 0:
        print("Turn: Player 2")
    else:
        print("Turn: Player 1")
    #announce how many sticks are on table
    print("There are", sticks, "sticks on the table.")
    #ask for valid input for how many sticks to take
    take = int(input("How many sticks do you want to take (1, 2 or 3)? "))
    while True:
        if take > 3 or take < 1:
            print("Sorry, that's not a valid number.")
            print()
            if turn % 2 == 0:
                print("Turn: Player 2")
            else:
                print("Turn: Player 1")
            print("There are", sticks, "sticks on the table.")
            take = int(input("How many sticks do you want to take (1, 2 or 3)? "))
        elif sticks - take < 0:
            print("Sorry, that would bring the total # of sticks below 0. Try again.")
            print()
            if turn % 2 == 0:
                print("Turn: Player 2")
            else:
                print("Turn: Player 1")
            print("There are", sticks, "sticks on the table.")
            take = int(input("How many sticks do you want to take (1, 2 or 3)? "))
        else:
            break
    print()
    #subtract amount of sticks taken from total
    sticks = sticks - take
    #loop until sticks reach zero
    if sticks == 0:
        break

#print game over
print("There are no sticks left on the table! Game over.")
#determine who won
if turn % 2 == 0:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")

