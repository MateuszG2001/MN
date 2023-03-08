import functions as fun
import matplotlib.pyplot as plt


def draw_function(which_function, start, end):
    x = [x * 0.001 for x in range(1000 * start, 1000 * end)]
    y = [which_function(i) for i in x]
    plt.plot(x, y)
    plt.grid(True)
    plt.axhline(0, color='black', linestyle='dashed')
    a = [i for i in x if 0.3 > which_function(i) > -0.3]
    plt.scatter(a, y=[0 for _ in range(0, len(a))], marker='o', s=50, color="red")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


draw_function(fun.f1, -5, 5)
draw_function(fun.f2, -5, 5)
draw_function(fun.f3, -5, 5)
