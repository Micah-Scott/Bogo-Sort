# Micah Scott 3/21/19

# imports
import random
import winsound
import time

# define some values
list = []
odetobogo = [329, 329, 349, 392, 392, 349, 329, 293, 261, 261, 293, 329, 293, 261, 261]
i = 0
p = 0

# get user input to append to list
print("Type numbers to be sorted:")
while i < 5:
    list.append(input())
    i += 1

# create a sorted copy of this list to check later
list2 = list.copy()
list2.sort()

# print function
def printList(list):
    for i in range(len(list)):
        print(list[i], end = " ")
    print()

# bogo sort
while True:
    winsound.Beep(odetobogo[p], 90)
    time.sleep(.1)
    printList(list)
    p += 1 

    # reset Beethoven
    if p >= 14:
        p = 0

    # check to if list is sorted
    if list == list2:
        print("list has been sorted.")
        winsound.Beep(880, 200)
        break
    
    # shuffle and repeat
    else:
        random.shuffle(list)
