def read_out(acrostic):
    new_word = ''
    for x in acrostic:
        if check_data_type(x):
            new_word = new_word + x[0]
    return new_word


def check_data_type(data):
    if isinstance(data, str):
        return True
    return False
