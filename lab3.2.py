from math import pi

def compare(x, y):
    field1 = countField(x)
    field2 = countField(y)
    if field1 > field2:
        print("Pole pierwszej figuy jest większe", field1)
    elif field1 == 0 and field2 == 0:
        print("Error error figury nie istnieją ;/")
    elif field1 == field2:
        print("Pola są równe", field1)
    else:
        print("Pole drugiej figury jest większe", field2)
def countField(x):
    if x[0] == "circle":
        if len(x) == 2:
            if x[1] > 0:
                r = x[1]
                field = round(pi*r**2, 2)
            else:
                print("Koło z bokami", x[1], "nie istnieje")
                field = 0
        else:
            field = 0
    elif x[0] == "rectangle":
        if len(x) == 3:
            if x[1] > 0 and x[2] > 0:
                d1 = x[1]
                d2 = x[2]
                field = d1 * d2
            else:
                print("Prostokąt z bokami", x[1], x[2], "nie istnieje")
                field = 0
        else:
            field = 0
    elif x[0] == "rhombus":
        if len(x) == 3:
            if x[1] > 0 and x[2] > 0:
                d1 = x[1]
                d2 = x[2]
                field = (d1*d2) / 2
            else:
                field = 0
                print("Romb z przekątnymi ", x[1], x[2], "nie istnieje")
        else:
            field = 0
    elif x[0] == "triangle":
        if len(x) == 3:
            if x[1] > 0 and x[2] > 0:
                a = x[1]
                h = x[2]
                field = (a * h) / 2
            else:
                field = 0
                print("Triangle with parameters ", x[1], x[2], "doesn't exist")
        else:
            field = 0
    else:
        print("There is no such figure to first figure:", x[0])
        field = 0
    return(field)
compare(['rhombus', 2, 3], ['circle', 15])