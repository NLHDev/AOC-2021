# Advent of Code Day 1.5
# Your goal now is to count the number of times the sum
# of measurements in this sliding window increases from the previous sum
#!/usr/bin/python

import sys

file = open("Day1Input.txt", "r")
depths = []
increases = 0

# Get input and place in list
for line in file:
    depths.append(line)

# Convert to list of Integers
depths = [int(i) for i in depths]

for x in range(len(depths)-3):
    sumA = depths[x] + depths[x+1] + depths[x+2]
    sumB = depths[x+1] + depths[x+2] + depths[x+3]

    if ( sumB > sumA):
        increases += 1

print(increases)

sys.exit(0)
