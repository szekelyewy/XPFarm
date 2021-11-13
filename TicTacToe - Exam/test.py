import random
import unittest

import numpy as np

import main


class TestClass(unittest.TestCase):

    def test_init_board(self):
        self.assertEqual([[0, 0, 0], [0, 0, 0], [0, 0, 0]], main.init_board())

    def test_init_board_negative(self):
        self.assertNotEqual([[1, 0, 0], [0, 0, 0], [0, 0, 0]], main.init_board())

    def test_set_up_board(self):
        input_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        output_board = """
    0|0|0
    -+-+-
    0|0|0
    -+-+-
    0|0|0
    """
        self.assertEqual(output_board, main.set_up_board(input_board))

    def test_negative_set_up_board(self):
        input_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        output_board = """
    0|0|0
    -----
    0|0|0
    -----
    0|0|0
    """
        self.assertNotEqual(output_board, main.set_up_board(input_board))

    def test_empty_spaces(self):
        input_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
                         main.empty_space(input_board))

    def test_no_empty_spaces(self):
        input_board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual([], main.empty_space(input_board))

    def test_pick_random(self):
        input_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        output_board = np.array([[0, 0, 0], [0, 0, 0], [1, 0, 0]])
        random.seed(0)
        self.assertTrue((output_board == main.pick_random(input_board, 1)).all())

    def test_row_win_player_1(self):
        input_board = np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]])
        self.assertTrue(main.row_win(input_board, 1))

    def test_row_win_player_2(self):
        input_board = np.array([[0, 0, 0], [2, 2, 2], [0, 0, 0]])
        self.assertTrue(main.row_win(input_board, 2))

    def test_no_row_win_player_1(self):
        input_board = np.array([[1, 0, 1], [0, 0, 0], [0, 0, 0]])
        self.assertFalse(main.row_win(input_board, 1))

    def test_no_row_win_player_2(self):
        input_board = np.array([[2, 2, 0], [0, 0, 0], [0, 0, 0]])
        self.assertFalse(main.row_win(input_board, 1))

    def test_col_win_player_1(self):
        input_board = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
        self.assertTrue(main.col_win(input_board, 1))

    def test_col_win_player_2(self):
        input_board = np.array([[0, 2, 0], [0, 2, 0], [0, 2, 0]])
        self.assertTrue(main.col_win(input_board, 2))

    def test_no_col_win_player_1(self):
        input_board = np.array([[1, 0, 0], [0, 0, 0], [1, 0, 0]])
        self.assertFalse(main.col_win(input_board, 1))

    def test_no_col_win_player_2(self):
        input_board = np.array([[2, 0, 0], [2, 0, 0], [0, 0, 0]])
        self.assertFalse(main.col_win(input_board, 1))