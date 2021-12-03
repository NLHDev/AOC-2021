# Advent of Code Day 1
# Count the number of times a depth measurement increases from the previous measurement
#!/usr/bin/python

import sys

file = open("Day1Input.txt", "r")
depths = []
increases = 0

for line in file:
    depths.append(line)

for x in range(len(depths)-1):
    if ( int(depths[x+1]) > int(depths[x])):
        increases += 1

print(increases)

sys.exit(0)
