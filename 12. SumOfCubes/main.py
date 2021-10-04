def sum_cubes(n):
    counter = 0
    if if_int(n) and if_positive(n):
        for x in range(1, n+1):
            counter += cubed_number(x)
    return counter


def if_positive(n):
    if n > 0:
        return True
    return False


def if_int(n):
    if isinstance(n, int):
        return True
    return False


def cubed_number(n):
    return pow(n, 3)
