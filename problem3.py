import math


def shuffle_strings(a, b):
    a_mid = math.ceil(len(a) / 2)
    b_mid = math.ceil(len(b) / 2)

    return (a[:a_mid] + b[:b_mid]) + (a[a_mid:] + b[b_mid:])


print(shuffle_strings('string', 'test'))
