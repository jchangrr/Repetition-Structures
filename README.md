# Repetition-Structures
Problem 1:
For this assignment you will be writing a program which first prompts the user for the number of sides to the dice they will be rolling. Your user should be limited to selecting dice with the following number of sides:
4 sides
6 sides
8 sides
10 sides
12 sides
20 sides
You can assume that that your user will enter integers when prompted. You will need to validate their input before you continue (i.e. entering -10 should cause your program to tell the user that their input is invalid). You should re-prompt the user to enter a value if they supply bad data. 
Next, your program should keep "rolling the dice" until the program generates a "snake eyes" roll (1 and 1). This means that you will roll two virtual dice of the specified size at a time. The program should "announce" every pair rolled and tell the user if the roll qualifies as one of the following:

A double roll (i.e. (2 and 2), (4 and 4), (6 and 6))
A high roll (i.e. on a six sided die, (6 and 6) )
A high/low roll (i.e. on a six sided die, (1 and 6) or (6 and 1)
An even roll (i.e. both die values are even: (2 and 2), (4 and 4))
An odd roll (i.e. both die values are odd: (3 and 3), (5 and 5))
A sum value (i.e. adding both die values together equals the size of the current die
Snake Eyes (1 and 1) - this should end the rolling portion of the program
At the end of the game you will want to calculate the average roll for each die and present this information to the user. 

Problem 2:
Part 1: For this assignment you will be creating an interface for two humans to play a simple game of "Pick Up Sticks". Here's how the game is played in the "real world":

The game begins with a number of sticks on a table (between 10 and 100)
Each player, in turn, takes between 1-3 sticks off the table.
The player to take the last stick loses.

Begin by asking the user for a number of sticks to be used in the game. Only accept numbers between 10 and 100 - if the user supplies a number outside of this range you should re-prompt them.

Next, continually announce to the user how many sticks are on the table and ask the user to enter in a number of sticks to take away. Only accept choices of 1,2 or 3 sticks - anything else should cause an error message to be displayed. Once a valid number of sticks has been entered you should deduct that # of sticks from the total number of sticks in the game. When you reach 0 sticks left the game is over

Part 2: As you can see, the single player version of this game isn't very fun. To make things more interesting we are now going to add in an element of competition. For this part you will be implementing a two player game where players take turns taking sticks from the table. The same rules apply - each player can only take 1, 2 or 3 sticks per turn. The player who takes the last stick off of the table is the loser.
