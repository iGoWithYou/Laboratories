from matplotlib.pyplot import *
def plot (y=int(input('Podaj dlugosc'))):
    x = []
    for i in range(y):
        x.append(i)
    matplotlib.pyplot.plot(x)
    show()

plot()