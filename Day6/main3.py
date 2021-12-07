# This is my THIRD solution
# Instead of modeling each FISH on its own, it keeps track of the TOTAL amount
# of fish per DAY.
# MUCH FASTER


day = 1
days_to_run = 256
initial_state = [4, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 3, 4, 1, 1, 1, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 3, 1, 1,
                 1, 5, 1, 2, 1, 1, 5, 3, 4, 2, 1, 1, 4, 1, 1, 5, 1, 1, 5, 5, 1, 1, 5, 2, 1, 4, 1, 2, 1, 4, 5, 4, 1, 1,
                 1, 1, 3, 1, 1, 1, 4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1,
                 2, 4, 4, 1, 1, 3, 1, 3, 2, 4, 3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 5, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1,
                 1, 2, 1, 1, 4, 1, 5, 1, 3, 1, 1, 1, 1, 1, 5, 1, 1, 1, 3, 1, 2, 1, 2, 1, 3, 4, 5, 1, 1, 1, 1, 1, 1, 5,
                 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 4, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 2, 1, 1, 1, 4, 2, 1, 1,
                 1, 4, 1, 1, 2, 3, 1, 4, 1, 5, 1, 1, 1, 2, 1, 5, 3, 3, 3, 1, 5, 3, 1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 3, 1,
                 1, 5, 1, 1, 1, 4, 1, 1, 5, 1, 2, 3, 4, 2, 1, 5, 2, 1, 2, 5, 1, 1, 1, 1, 4, 1, 2, 1, 1, 1, 2, 5, 1, 1,
                 5, 1, 1, 1, 3, 2, 4, 1, 3, 1, 1, 2, 1, 5, 1, 3, 4, 4, 2, 2, 1, 1, 1, 1, 5, 1, 5, 2
                 ]
angler = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in initial_state:
    angler[i] += 1
# angler = [0, 1, 1, 2, 1, 0, 0, 0, 0]
print(angler)


while day <= days_to_run:
    print(angler)
    temp = angler[0]
    for i in range(8):
        angler[i] = angler[i + 1]
    angler[8] = temp
    angler[6] += temp

    total_fish = 0
    for i in angler:
        total_fish += i
    print("Total number of fish = ", total_fish)
    day += 1
