import matplotlib.pyplot as plt


class Function:
    """
    A class representing a mathematical function.
    """
    def __init__(self, evaluator, derivative, x_min, x_max, label):
        """
        :param evaluator: A lambda expression representing the function, which takes a value of x as input and returns
        the corresponding y value
        :param derivative: A lambda expression representing the derivative of the function, which takes a value of x as
        input and returns the corresponding slope
        :param x_min: The starting point of the interval for plotting the function
        :param x_max: The ending point of the interval for plotting the function
        :param label: A string representing the function in human-readable format
        """
        self.evaluator = evaluator
        self.derivative = derivative
        self.x_min = x_min
        self.x_max = x_max
        self.label = label

    def __str__(self):
        return self.label

    def __call__(self, x):
        return self.evaluator(x)

    def get_derivative(self):
        return self.derivative

    def plot(self, roots=None, markers=None, colors=None, step=0.001):
        if roots is None:
            roots = []
        if markers is None:
            markers = []
        if colors is None:
            colors = []

        x = [i * step for i in range(int(1 / step) * self.x_min, int(1 / step) * self.x_max)]
        y = [self(i) for i in x]

        plt.axhline(0, color='black', linestyle='dashed')
        plt.plot(x, y)
        plt.grid(True)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(self)

        for i in range(0, len(roots)):
            plt.scatter(roots[i], 0, marker=markers[i], color=colors[i], s=250)

        plt.show()
