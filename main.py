import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

def f(x1,x2):
    return (1-(x1**2+x2**3))*np.exp(-(x1**2+x2**2)/2)


def cmp_t(w, T):
    if w[0] > T:
        w[0] = T
    if w[1] > T:
        w[1] = T
    if w[0] < -T:
        w[0] = -T
    if w[1] < -T:
        w[1] = -T
    return w


def generate_figure(X,Y, y):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.contour3D(X, Y,y, 100)
    ax.view_init(1, 1)

    plt.title("Visual representation of function" , fontsize=8)
    plt.savefig("visual_representation.png", bbox_inches='tight')
    plt.show(block=False)
    plt.pause(2)
    plt.close()


def show_current_results(X, Y, y, results,fig, ax):
    ax.contour(X, Y, y)
    x1,y1 = zip(*results)
    ax.plot(x1, y1, 'k-')
    dot, =ax.plot(results[-1][0], results[-1][1], 'ro')
    ax.cmap.set_over('red')
    ax.cmap.set_under('blue')
    ax.changed()
    ax.set_title('Results')
    display(fig)    
    clear_output(wait = True)
    plt.pause(0.1)

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
fig, ax = plt.subplots()
w = 2*T*np.random.rand(2,1) - T
E = f(w[0], w[1])

for i in range(1,n_iterations+1):
    dw = np.random.rand(2,1) * T
    w2 = w + dw
    w2 = cmp_t(w2, T)

    E2 = f(w2[0], w2[1])
    dE = E2 - E 
    rand_n = np.random.rand()
    computed_data = (1/(1+np.exp(dE/(c*T))))
    if rand_n < computed_data:
        E = E2
        w = w2
        list_w = w.tolist()
        list_w[0] = list_w[0][0]
        list_w[1] = list_w[1][0]

        results.append(list_w)
    T = T*correction_rate
    if T < Tmin:
        T = Tmin
    
    temperatures.append(T)

    if i % 10 == 0:
        show_current_results(X, Y, y, results, fig, ax)