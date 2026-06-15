from time import sleep
from math import sqrt

a = input("First Value: ")
b = input("End Value: ")

try:
    a = int(a)
    b = int(b)
except ValueError:
    print("Error: First Value and End Value must be filled and must be a number")
else:
    if a >= 2 and a < b:
        print("Prime Numbers: ", end="")
        while a <= b:
            p = None
            c = a // 2
            sa = sqrt(a)

            if a <= 3:
                print(a, end=" ")
                a += 1
            elif a % 2 == 0:
                a += 1
            elif sa == int(sa):
                a += 2
            elif c >= 2:
                for i in range(3, c + 1, 2):
                    if a % i == 0:
                        p = False
                        break
                
                if p == None:
                    print(a, end=" ")
                a += 2

        print()
        print()
        print("Done.")
    else:
        print("Error: Sorry, the Program cannot be run because First Value is less than 2 or higher than End Value")

input("Tekan Enter untuk keluar")