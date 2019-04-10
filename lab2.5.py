import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from cs50 import get_float

n = get_float("zmien częstotliwość ")
m = get_float("zmien amplitude")
if n == 0:
    if m == 0:
        x_knots = np.linspace(-3*np.pi,3*np.pi,201)
        y_knots = np.linspace(-3*np.pi,3*np.pi,201)
        X, Y = np.meshgrid(x_knots, y_knots)
        #R = X + Y
        R = np.sqrt(X**2+Y**2)
        Z = np.cos(R)**2*np.exp(-0.1*R)
        ax = Axes3D(plt.figure(figsize=(8,5)))
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
        plt.show()
    else:
        x_knots = np.linspace(-3 * np.pi, 3 * np.pi, 201)
        y_knots = np.linspace(-3 * np.pi, 3 * np.pi, 201)
        X, Y = np.meshgrid(x_knots, y_knots)
        # R = X + Y
        R = np.sqrt(X ** 2 + Y ** 2)
        Z = (np.cos(R) / m) ** 2 * np.exp(-0.1 * R)
        ax = Axes3D(plt.figure(figsize=(8, 5)))
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
        plt.show()
else:
    if m == 0:
        x_knots = np.linspace(-3 * np.pi, 3 * np.pi, 201)
        y_knots = np.linspace(-3 * np.pi, 3 * np.pi, 201)
        X, Y = np.meshgrid(x_knots, y_knots)
        # R = X + Y
        R = np.sqrt(X ** 2 + Y ** 2)
        Z = (np.cos(R * n)) ** 2 * np.exp(-0.1 * R)
        ax = Axes3D(plt.figure(figsize=(8, 5)))
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
        plt.show()
    else:
        x_knots = np.linspace(-3 * np.pi, 3 * np.pi, 201)
        y_knots = np.linspace(-3 * np.pi, 3 * np.pi, 201)
        X, Y = np.meshgrid(x_knots, y_knots)
        # R = X + Y
        R = np.sqrt(X ** 2 + Y ** 2)
        Z = (np.cos(R * n) / m) ** 2 * np.exp(-0.1 * R)
        ax = Axes3D(plt.figure(figsize=(8, 5)))
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
        plt.show()