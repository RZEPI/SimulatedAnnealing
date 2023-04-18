import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def f(x1,x2):
    return (1-(x1**2+x2**3))*np.exp(-(x1**2+x2**2)/2)


def generate_figure(X,Y, y):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.contour3D(X, Y,y, 100)
    ax.view_init(1, 1)

    plt.title("Visual representation of function" , fontsize=8)
    plt.savefig("visual_representation.png", bbox_inches='tight')
    plt.show()
    plt.close()


n_iterations = 500
T = 10
Tmin = 0.001
c = 0.2
correction_rate = 0.99
results = []
temperatures = []

[X, Y] = np.meshgrid(np.arange(-T,T, 0.1),np.arange(-T,T, 0.1))
y = f(X, Y)

generate_figure(X, Y, y)

w = 2*T*np.random.rand(2,1) - T
E = f(w[0], w[2])


