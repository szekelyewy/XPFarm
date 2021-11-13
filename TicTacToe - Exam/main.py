def init_board():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def set_up_board(input_board):
    board_template = """
    {}|{}|{}
    -+-+-
    {}|{}|{}
    -+-+-
    {}|{}|{}
    """
    a = [item for sub in input_board for item in sub]
    return board_template.format(*a)
