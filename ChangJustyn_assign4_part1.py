"""
Assignment #4, Problem #1
Justyn Chang
"""
#ask for valid input on how many sides on dice
sides = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))
while True:
    if sides == 4 or sides == 6 or sides == 8 or sides == 10 or sides == 12 or sides == 20:
        break
    print("Invalid size, try again")
    sides = int(input("how many sides on your dice (4, 6, 8, 10, 12 or 20)? "))

print()
print("Thanks, here we go!")
print()

#generate random dice rolls
import random
die1 = random.randint(1, sides)
die2 = random.randint(1, sides)
count = 0
evens = 0
odds = 0
high = 0
highlow = 0
doubles = 0
sumvalue = 0
die1_sum = 0
die2_sum = 0

while True:
    #increase roll count
    count += 1
    #announce dice numbers
    print(count, ". die #1 is *", die1, "* and die #2 is *", die2, "*", sep = "", end = "")
    die1_sum = die1_sum + die1
    die2_sum = die2_sum + die2
    #determine if evens
    if die1 % 2 == 0 and die2 % 2 == 0:
        print(" Evens!", end = "")
        evens += 1
    #determine if odds
    elif die1 % 2 != 0 and die2 % 2 != 0:
        print(" Odds!", end = "")
        odds += 1
    #determine if dice are equal to each other
    if die1 == die2:
        print(" Doubles!", end = "")
        doubles += 1
    #determine if dice are highs
    if die1 == sides and die2 == sides:
        print(" High!", end = "")
        high += 1
    #determine if dice are high/low
    if (die1 == sides and die2 == 1) or (die1 == 1 and die2 == sides):
        print(" High / Low!", end = "")
        highlow += 1
    #determine if dice are sum value
    if die1 + die2 == sides:
        print(" Sum value is size value!", end = "")
        sumvalue += 1
    #determine if dice are snake eyes
    if die1 == 1 and die2 == 1:
        print(" Snake Eyes!")
        break
    #generate new roll if no snake eyes
    die1 = random.randint(1, sides)
    die2 = random.randint(1, sides)
    print()

#calculate percent of each outcome and avg roll for each die
print()
doubles_percent = format(100 * float(float(doubles) / float(count)), ".2f")
high_percent = format(100 * float(float(high) / float(count)), ".2f")
evens_percent = format(100 *float(float(evens) / float(count)), ".2f")
odds_percent = format(100 * float(float(odds) / float(count)), ".2f")
highlow_percent = format(100 * float(float(highlow) / float(count)), ".2f")
sumvalue_percent = format(100 * float(float(sumvalue) / float(count)), ".2f")
die1_avg = format(float(float(die1_sum) / float(count)), ".2f")
die2_avg = format(float(float(die2_sum) / float(count)), ".2f")

#print results
print("You finally got snake eyes on roll #", count)
print("Along the way you rolled DOUBLES ", doubles, " times. (", doubles_percent, "% of all rolls were doubles)", sep = "")
print("Along the way you rolled TWO HIGH VALUES ", high, " times. (", high_percent, "% of all rolls were two high values)", sep = "")
print("Along the way you rolled TWO EVENS ", evens, " times. (", evens_percent, "% of all rolls were two evens)", sep = "")
print("Along the way you rolled TWO ODDS ", odds, " times. (", odds_percent, "% of all rolls were two odds)", sep = "")
print("Along the way you rolled HIGH / LOW ", highlow, " times. (", highlow_percent, "% of all rolls were high/low)", sep = "")
print("Along the way you rolled A SUM VALUE ", sumvalue, " times. (", sumvalue_percent, "% of all rolls were a sum value)", sep = "")
print("Average roll for die #1:", die1_avg)
print("Average roll for die #2:", die2_avg)
