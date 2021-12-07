#!/usr/bin/Python
# This is my FIRST solution which works well for... small numbers of fish but will exponentially use more RAM on larger numbers

class Fish:

    def __init__(self, timer=8):
        self.timer = timer

    def dec_day(self):
        if self.timer == 0:
            self.timer = 6
            angler.append(Fish(9))
        else:
            self.timer -= 1


if __name__ == '__main__':

    days_to_run = 18
    initial_state = [3, 4, 3, 1, 2]

    day = 1
    angler = []

    # Set initial state
    for i in range(len(initial_state)):
        angler.append(Fish(initial_state[i]))
    # Print Initial State
    # print("Initial State: ", end=" ")
    # for fish in angler:
        # print(fish.timer, end=",")
    # print()

    # Begin main countdown loop
    while day <= days_to_run:
        # print("After ", day, " days:", end=" ")
        for fish in angler:
            fish.dec_day()
            # print(fish.timer, end=",")
        # print()
        day += 1
        print(day)
    print("Total number of fish =", len(angler))
