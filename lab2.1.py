from cs50 import get_int, get_float, get_string
from math import pi
while True:
    y = get_float("y: ")
    if y > 0:
        break
    else:
        print("Circle with radius:", y, "doesnt exist, enter diffrent radius")
while True:
    x = get_float("x: ")
    if x > 0:
        break
    else:
        print("Circle with radius:", x, "doesnt exist, enter diffrent radius")

PerimeterXcircle = 2 * pi * x
FieldX = pi * x ** 2
print("Perimeter X circle: ", PerimeterXcircle, "Field X circle: ", FieldX)
PerimeterYcircle = 2 * pi * y
FieldY = pi * y ** 2
print("Perimeter Y circle: ", PerimeterYcircle, "Field Y circle: ", FieldY)




