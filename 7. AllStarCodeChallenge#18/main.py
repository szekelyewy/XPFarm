def str_count(strng, letter):
    count = 0
    if check_if_string(strng) and check_if_string(letter):
        for x in strng:
            if letter in x:
                count += 1
    return count


def check_if_string(string):
    if isinstance(string, str):
        return True
    return False
