from time import sleep
from turtle import *

amount = input("Amount: ")
size = input("Size: ")

try:
    amount = int(amount)
    size = float(size)
except ValueError:
    print("Error: Please enter a valid number")
    sleep(1)
else:
    if amount <= 1 or size <= 0:
        print("Error: Please enter valid values")
        sleep(1)
        exit()

    total = amount * size

    right(90)
    up()
    forward(total / 2)
    left(90)
    down()
    forward(total - size / 2)
    left(90)

    for i in range(amount):
        forward(size)
        left(90)
        forward(size)
        right(90)

    left(180)

    for i in range(amount - 1):
        forward(size)
        right(90)
        forward(size)
        left(90)

    forward(size)
    left(90)
    forward(total - size / 2 + size)
    backward(total - size / 2)

    for i in range(amount - 1):
        left(90)
        forward(size * (i + 1))
        backward(size * (i + 1))
        right(90)
        forward(size)

    for i in range(amount - 1):
        left(90)
        forward(total - size * (i + 1))
        backward(total - size * (i + 1))
        right(90)
        forward(size)
    
    left(90)
    pensize(2.5)

    for i in range(amount):
        forward(size)
        left(90)
        forward(size)
        forward(total * 2 - size * 2 * (i + 1))
        backward(total * 2 - size * 2 * (i + 1))
        right(90)

    left(180)

    for i in range(amount - 1):
        forward(size)
        right(90)
        forward(size)
        left(90)
    
    forward(size)
    left(90)
    forward((total - size / 2) * 2)

sleep(2)