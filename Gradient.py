import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output


class Gradient:
    ETA = 0.5
    results = []
    bound = 10

    def __init__(self, function, diff_fun, iterations):
        self.function = function
        self.diff_fun = diff_fun
        self.n_iterations = iterations

    def show_current_results(self, X, Y, y, fig, ax):
        ax.contourf(X, Y, y)
        x1, y1 = zip(*self.results)
        ax.plot(x1, y1, 'k-')
        ax.set_title('Gradient Method')
        display(fig)
        clear_output(wait=True)
        plt.pause(0.1)

    def parse_component(self, comp):
        if comp < -self.bound:
            comp = -self.bound
        if comp > self.bound:
            comp = self.bound
        return comp 

    def start(self):
        w = np.random.rand(2, 1)*10
        fig, ax = plt.subplots()
        [X, Y] = np.meshgrid(np.arange(-self.bound, self.bound, 0.1), np.arange(-self.bound, self.bound, 0.1))
        Z = self.function(X, Y)
        for i in range(1, self.n_iterations+1):
            diff_values = self.diff_fun(w[0], w[1])
            x = w[0] - self.ETA**i*diff_values[0]
            y = w[1] - self.ETA**i*diff_values[1]
            w = [x, y]
            try:
                if w == self.results[-1]:
                    break
            except:
                pass
            self.results.append([self.parse_component(x), self.parse_component(y)])
            self.show_current_results(X, Y, Z, fig, ax)

    def get_results(self):
        return self.results
