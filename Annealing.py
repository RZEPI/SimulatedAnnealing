import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

class Annealing:
    temperature = 10
    T_MIN = 0.001
    C = 0.2
    CORRECTION_RATE = 0.99
    results = []
    temperatures = []

    def __init__(self, fun, iterations):
        self.function = fun 
        self.n_iterations = iterations

    def generate_figure(self, X,Y, y):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.contour3D(X, Y, y, 100)
        ax.view_init(1, 1)

        plt.title("Visual representation of function" , fontsize=8)
        plt.savefig("visual_representation.png", bbox_inches='tight')
        plt.show(block=False)
        plt.pause(2)
        plt.close()


    def show_current_results(self, X, Y, y,fig, ax):
        ax.contourf(X, Y, y)
        x1,y1 = zip(*self.results)
        ax.plot(x1, y1, 'k-')
        ax.set_title('Simulated Annealing Method')
        display(fig)    
        clear_output(wait = True)
        plt.pause(0.1)


    def cmp_t(self, w):
        if w[0] > self.temperature:
            w[0] = self.temperature
        if w[1] > self.temperature:
            w[1] = self.temperature
        if w[0] < -self.temperature:
            w[0] = -self.temperature
        if w[1] < -self.temperature:
            w[1] = -self.temperature
        return w



    def start(self):
        [X, Y] = np.meshgrid(np.arange(-self.temperature,self.temperature, 0.1), \
                             np.arange(-self.temperature,self.temperature, 0.1))
        y = self.function(X, Y)

        self.generate_figure(X, Y, y)
        fig, ax = plt.subplots()
        w = 2*self.temperature*np.random.rand(2,1) - self.temperature
        E = self.function(w[0], w[1])

        for i in range(1,self.n_iterations+1):
            dw = np.random.randn(2,1) * self.temperature
            w2 = w + dw
            w2 = self.cmp_t(w2)

            E2 = self.function(w2[0], w2[1])
            dE = E2 - E 
            rand_n = np.random.rand()
            computed_data = (1/(1+np.exp(dE/(self.C*self.temperature))))
            if rand_n < computed_data:
                E = E2
                w = w2
                list_w = w.tolist()
                list_w[0] = list_w[0][0]
                list_w[1] = list_w[1][0]

                self.results.append(list_w)
            self.temperature = self.temperature*self.CORRECTION_RATE
            if self.temperature < self.T_MIN:
                self.temperature = self.T_MIN
            
            self.temperatures.append(self.temperature)

            if i % 10 == 0:
                self.show_current_results(X, Y, y, fig, ax)

    def get_results(self):
        return self.results