def between(a, b):
    if is_bigger(a, b):
        between_array = []
        for x in range(a + 1, b):
            between_array.append(x)
        return between_array


def is_bigger(a, b):
    if a < b:
        return True
    else:
        return False
