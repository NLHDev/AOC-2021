#!/usr/bin/python
# Advent of Code Day 2
# Calculate the horizontal position and depth you would
# have after following the planned course.


import sys
# Get input and place in list
file = open("Day2Input.txt", "r")

# Subs starting position is 0,0 (x,y)
position = [0, 0]

for line in file:
    newline = line.split()
    if (newline[0] == "forward"):
        position[0] = position[0] + int(newline[1])
    elif (newline[0] == "down"):
        position[1] = position[1] + int(newline[1])
    elif (newline[0] == "up"):
        position[1] = position[1] - int(newline[1])

print(position)
print(position[0] * position[1])

sys.exit(0)
