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


def empty_space(input_board):
    empty_spaces = []
    for i in range(len(input_board)):
        for j in range(len(input_board)):

            if input_board[i][j] == 0:
                empty_spaces.append((i, j))
    return empty_spaces
