def is_triangle(a, b, c):
    if if_int(a) and if_int(b) and if_int(c) and if_positive(a) and if_positive(b) and if_positive(c):
        if a + b > c and a + c > b and c + b > a:
            return True
    return False


def if_int(n):
    if isinstance(n, int):
        return True
    return False


def if_positive(n):
    if n > 0:
        return True
    return False
