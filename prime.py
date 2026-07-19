from time import sleep
from math import sqrt

firstValue = input("First Value: ")
endValue = input("End Value: ")

try:
    firstValue = int(firstValue)
    endValue = int(endValue)
except ValueError:
    print("Error: First Value and End Value must be filled and must be firstValue number")
else:
    if firstValue >= 2 and firstValue < endValue:
        count = 0
        percentage = 0
        counting = firstValue

        print("Prime Numbers: ", end="")
        while counting <= endValue:
            a = counting // 2
            b = sqrt(counting)

            if counting <= 3:
                print(counting, end=" ")
                counting += 1
                count += 1
            elif counting % 2 == 0:
                counting += 1
            elif b == int(b):
                counting += 2
            elif a >= 2:
                p = None
                for i in range(3, a + 1, 2):
                    if counting % i == 0:
                        p = False
                        break
                
                if p == None:
                    print(counting, end=" ")
                    count += 1
                counting += 2

        print()
        percentage = (count / (endValue - firstValue + 1)) * 100
        print(f"Total prime numbers found: {count}")
        print(f"Percentage of prime numbers: {percentage:.2f}%")
        print()
        print("Done")
    else:
        print("Error: Sorry, the Program cannot be run because First Value is less than 2 or higher than End Value")

input("Press ENTER to exit")