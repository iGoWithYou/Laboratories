from cs50 import get_int, get_float, get_string
#from decimal import *
x = get_float("x: ")
while True:
    y = get_float("y: ")
    if y == 0:
        print("nie dziel przez 0")
    else:

        z = x /y
        break
#z = round(double(x / y), 100)
#d = format(z, '.100f')
#print(z)
print(round(z, 2))
