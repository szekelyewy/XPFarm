def square_digits(num):
    new_number= ''
    if check_data_type(num):
        for x in str(num):
            new_number = new_number + str(pow(int(x), 2))
    new_number = int(new_number)
    return new_number


def check_data_type(num):
    if isinstance(num, int):
        return True
    return False
