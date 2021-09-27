def open_or_senior(data):
    return ["Senior" if check_valid_handicap_range(handicap) and check_if_older_than_55(age)
            and check_if_handicap_greater_than_7(handicap) else "Open" for (age, handicap) in data]


def check_if_older_than_55(number):
    if number >= 55:
        return True
    return False


def check_if_handicap_greater_than_7(number):
    if number > 7:
        return True
    return False


def check_valid_handicap_range(number):
    if -2 <= number <= 26:
        return True
    return False
