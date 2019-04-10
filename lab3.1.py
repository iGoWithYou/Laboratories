from math import pi
figure = []
figure.append(str(input("Choose your figure circle/rectangle/triangle/rhombus: ")))
figure.append(int(float(input("enter the parameter - radius or first side or first diagonal or base: "))))
for i in range(len(figure)):
    if figure[i] == "rectangle" or figure[i] == "triangle" or figure[i] == "rhombus":
        figure.append(int(float(input("enter the parameter - second side or second diagonal or height: "))))
    else:
        figure = figure
def countField(y):
    if y[0] == "circle":
        if y[1] > 0:
            r = y[1]
            field = pi*r**2
            print("Our circle field = ", field)
        else:
            print("The circle doesn't exist :D")
    elif y[0] =="rectangle":
        if y[1] > 0 and y[2] > 0:
            x = y[1]
            y = y[2]
            field = x*y
            print("Our rectangle field = ", field)
        else:
            print("The rectangle doesn't exist :D")
    elif y[0] == "rhombus":
        if y[1] > 0 and y[2] > 0:
            d1 = y[1]
            d2 = y[2]
            field = (d1*d2) / 2
            print("The rhombus field = ", round(field, 2))
        else:
            print("The rhombus doesn't exist")
    elif y[0] == "triangle":
        if y[1] > 0 and y[2] > 0:
            a = y[1]
            h = y[2]
            field = (a * h) / 2
            print ("The triangle field = ", field)
        else:
            print("The triangle doesn't exist'")
    else:
        print("There is no such figure")
countField(figure)