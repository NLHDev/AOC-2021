#!/usr/bin/python
# Advent of Code Day 3
#


import sys
# Get input and place in list
file = open("Day3InputTest.txt", "r")
#file = open("Day3Input.txt", "r")

# These will hold the total ones and zeros of all the binary input

onesum = [0, 0, 0, 0, 0] #, 0, 0, 0, 0, 0, 0, 0]
zerosum = [0, 0, 0, 0, 0] #, 0, 0, 0, 0, 0, 0, 0]
oxygen = []

# Go through every line of the file and add up how many 1s and 0s are in each
# column.
for line in file:
    oxygen.append(line[0:5]) # Create a list of all the input
    diag = [int for int in line]
    for i in range(len(diag)-1):
        if diag[i] == '0':
            zerosum[i] += 1
        elif diag[i] == '1':
            onesum[i] += 1

# Calculate the most common value in each bit position, save that as a new list
common = []
for i in range(len(zerosum)):
    if (zerosum[i] > onesum[i]):
        common.append('0')
    else:
        common.append('1')
print(common)
print(oxygen)

# Calculate Oxygen Generator Rating
oxygenproc = []
i = 0
for line in oxygen:
    temp = str(line[:1])
    if temp == common[i]:
        oxygenproc.append(temp)
        print(oxygenproc)
    i += 1

sys.exit(0)
