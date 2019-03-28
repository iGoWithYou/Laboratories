from cs50 import get_int, get_float, get_string
while True:
    while True:
        x = get_float("x: ")
        if (x % 2) == 0:
            print("x is even",x)
            break
        else:
            print("x isnt even try again")

    while True:
        y = get_float("y: ")
        if (y % 2) == 0:
            print("y is even",x)
            break
        else:
            print("y isnt even try again")
    if x % y == 0:
        print("x is divisible by y")
        break
    else:
        print("x isnt divisible by y, try again")
