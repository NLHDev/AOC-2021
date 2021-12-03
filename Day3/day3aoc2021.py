#!/usr/bin/python
# Advent of Code Day 3
#


import sys
# Get input and place in list
file = open("Day3Input.txt", "r")
#file = open("Day3Input.txt", "r")

# These will hold the total ones and zeros of all the binary input

onesum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zerosum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Go through every line of the file and add up how many 1s and 0s are in each
# column.
for line in file:
    diag = [int for int in line]
    for i in range(len(diag)-1):
        if diag[i] == '0':
            zerosum[i] += 1
        elif diag[i] == '1':
            onesum[i] += 1
    #print(diag)

# Calculate the 'gamma' and 'epsilon' numbers
gamma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
epsilon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(onesum)):
    if (onesum[i] > zerosum[i]):
        gamma[i] = 1
        epsilon[i] = 0
    else:
        gamma[i] = 0
        epsilon[i] = 1

# Convert the 'binary' numbers (which are int lists) to actual decimal numbers
gamma.reverse()
decgam = 0
epsilon.reverse()
deceps = 0
for i in range(len(gamma)):
    decgam += gamma[i] * (2 ** i)
    deceps += epsilon[i] * (2 ** i)

print('Power consumption is: ' + str(decgam * deceps))
sys.exit(0)
