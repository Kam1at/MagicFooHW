import math


class Derivative():
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        return math.cos(args[0])


def sin_(x):
    return math.sin(x)


print(sin_(math.pi / 3))


@Derivative
def sin_(x):
    return math.sin(x)


print(sin_(math.pi / 3))