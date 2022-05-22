import math


def calc_distance(x1, x2, y1, y2):
    return math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))


print(calc_distance(1, 2, 3, 4))
