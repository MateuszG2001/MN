def find_root_using_bisection_method(func, start, end, **kwargs):
    """
    Finds the approximation of the root of the given function in the given interval using the bisection method.
    If the optional keyword argument `epsilon` is provided, the algorithm finishes as soon as the absolute value of the
    function for the computed root is less than the value of this argument. Otherwise, if the `iterations` argument is
    provided, the algorithm finishes after a number of iterations equal to the value of this argument. If none of these
    keyword arguments are provided, the algorithm finishes after 10 iterations. If both of the keyword arguments are
    provided, an exception is raised.

    :param func: A function whose root we are looking for
    :param start: The beginning of the interval in which we are looking for the root
    :param end: The end of the interval in which we are looking for the root
    :param kwargs: Keyword arguments: `epsilon` or `iterations`.
    :return: An approximate value of the argument from the given range, for which the value of the function is 0.
    """

    if kwargs.get('epsilon') and kwargs.get('iterations'):
        raise Exception('Both epsilon and iterations were provided')

    if func(start)*func(end) >= 0:
        raise Exception('Invalid interval')

    i = 0
    x = None
    epsilon = kwargs.get('epsilon') if kwargs.get('epsilon') else 0
    iterations = kwargs.get('iterations') if kwargs.get('iterations') else -1

    while abs(start - end) > epsilon:
        x = (start + end) / 2

        if abs(func(x)) <= epsilon or i == iterations:
            break
        elif func(x)*func(start) < 0:
            end = x     # Continue searching in the left half of the interval
        else:
            start = x   # Continue searching in the right half of the interval

        i += 1

    return x
