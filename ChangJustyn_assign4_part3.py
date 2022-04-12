"""
Assignment #4, Problem #3
Justyn Chang
"""
#record program start time
import time
time1 = time.time()
#ask for valid input for number of throws
while True:
    totalthrows = int(input("Number of throws: "))
    if totalthrows < 0:
        print("Invalid, try again!")
    else:
        break
print()

throw = 0
miss = 0
red = 0
blue = 0
green = 0
darkgrey = 0
lightgrey = 0
miss = 0
import random
while True:
    #generate random dart throw on x and y coordinates
    throw += 1
    throw_x = random.uniform(1, 800)
    throw_y = random.uniform(1, 500)
    import math
    #calculate distances from center of the circles
    blue_dist = math.sqrt(math.pow(throw_x - 400, 2) + math.pow(throw_y - 150, 2))
    darkgrey1_dist = math.sqrt(math.pow(throw_x - 150, 2) + math.pow(throw_y - 300, 2))
    darkgrey2_dist = math.sqrt(math.pow(throw_x - 150, 2) + math.pow(throw_y - 200, 2))
    #determine if dart landed in red
    if throw_x >= 350 and throw_x <= 450 and throw_y >= 300 and throw_y <= 450:
        red += 1
    #determine if dart landed in blue using distance from center of blue circle
    elif blue_dist <= 100:
        blue += 1
    #determine if dart landed in light grey using distances from center of the dark grey circles
    elif darkgrey1_dist <= 100 and darkgrey2_dist <= 50:
        lightgrey += 1
    #determine if dart landed in dark grey using distances from center of the dark grey circles
    elif darkgrey1_dist <= 100 or darkgrey2_dist <= 50:
        darkgrey += 1
    #determine if dart landed in green
    elif throw_x >= 550 and throw_x <= 750 and throw_y >= 50 and throw_y <= 750:
        if throw_x >= 600 and throw_x <= 700 and throw_y >= 100 and throw_y <= 200:
            miss += 1
        elif throw_x >= 600 and throw_x <= 650 and throw_y >= 250 and throw_y <= 300:
            miss += 1
        elif throw_x >= 650 and throw_x <= 700 and throw_y >= 650 and throw_y <= 700:
            miss += 1
        else:
            green += 1
    #if none of the above is true, then dart missed
    else:
        miss += 1
    #break loop when number of throws equals the desired amount by user
    if throw == totalthrows:
        break

#calculate percent of each outcome
red_percent = format(100 * float(red / throw), ".2f")
blue_percent = format(100 * float(blue / throw), ".2f")
green_percent = format(100 * float(green / throw), ".2f")
darkgrey_percent = format(100 * float(darkgrey / throw), ".2f")
lightgrey_percent = format(100 * float(lightgrey / throw), ".2f")
miss_percent = format(100 * float(miss / throw), ".2f")

#format strings to align them
red = format(str(red), ">17s")
blue = format(str(blue), ">16s")
green = format(str(green), ">15s")
darkgrey = format(str(darkgrey), ">11s")
lightgrey = format(str(lightgrey), ">10s")
miss = format(str(miss), ">14s")
#record program end time
time2 = time.time()
time = format(time2 - time1, ".2f")

#print results
print("Total time elapsed:", time, "seconds")
print("Red:", red, " (", red_percent, "%)", sep = "")
print("Blue:", blue, " (", blue_percent, "%)", sep = "")
print("Green:", green, " (", green_percent, "%)", sep = "")
print("Dark Grey:", darkgrey, " (", darkgrey_percent, "%)", sep = "")
print("Light Grey:", lightgrey, " (", lightgrey_percent, "%)", sep = "")
print("Misses:", miss, " (", miss_percent, "%)", sep = "")
