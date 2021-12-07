# This is my SECOND solution which... doesn't do much better on RAM and will crash on high numbers of fish. Had to change my approach

days_to_run = 256
angler = [3, 4, 3, 1, 2]
day = 1

while day <= days_to_run:
    for i in range(len(angler)):
        if angler[i] == 0:
            angler[i] = 6
            angler.append(8)
        else:
            angler[i] -= 1
    print(day)
    day += 1
print("Total number of fish = ", len(angler))
