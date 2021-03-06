import random

import numpy as np


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


def pick_random(input_board, player):
    choices = empty_space(input_board)
    choice = random.choice(choices)
    numpy_board = np.array(input_board)
    numpy_board[choice] = player
    return numpy_board


def row_win(input_board, player_number):
    for element_x in range(len(input_board)):
        win = True
        for element_y in range(len(input_board)):
            if input_board[element_x, element_y] != player_number:
                win = False
                continue
        if win:
            return win


def col_win(input_board, player):
    for x in range(len(input_board)):
        win = True
        for y in range(len(input_board)):
            if input_board[y][x] != player:
                win = False
                continue
        if win:
            return win


def diag_win(input_board, player):
    win = True
    y = 0
    for x in range(len(input_board)):
        if input_board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(input_board)):
            y = len(input_board) - 1 - x
            if input_board[x, y] != player:
                win = False
    return win
