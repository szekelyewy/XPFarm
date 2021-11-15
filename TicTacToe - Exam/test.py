import random
import unittest

import numpy as np

import main


class TestClass(unittest.TestCase):

    def test_init_board(self):
        """Checks if the initial board is an empty 3x3 array"""
        self.assertEqual([[0, 0, 0], [0, 0, 0], [0, 0, 0]], main.init_board())

    def test_init_board_negative(self):
        """Negative test for initial board"""
        self.assertNotEqual([[1, 0, 0], [0, 0, 0], [0, 0, 0]], main.init_board())

    def test_set_up_board(self):
        """Checks the template of the initial board"""
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
        """Negative test for the board template"""
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
        """Checks if the empty spaces calculated correctly"""
        input_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
                         main.empty_space(input_board))

    def test_no_empty_spaces(self):
        """Negative test for the empty spaces"""
        input_board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual([], main.empty_space(input_board))

    def test_pick_random(self):
        """Checks the random picker with a seeded value"""
        input_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        output_board = np.array([[0, 0, 0], [0, 0, 0], [1, 0, 0]])
        random.seed(0)
        self.assertTrue((output_board == main.pick_random(input_board, 1)).all())

    def test_row_win_player_1(self):
        """Tests if player 1 won with the first row"""
        input_board = np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]])
        self.assertTrue(main.row_win(input_board, 1))

    def test_row_win_player_2(self):
        """Tests if player 2 won with the second row"""
        input_board = np.array([[0, 0, 0], [2, 2, 2], [0, 0, 0]])
        self.assertTrue(main.row_win(input_board, 2))

    def test_no_row_win_player_1(self):
        """Tests if no row win happened for player 1"""
        input_board = np.array([[1, 0, 1], [0, 0, 0], [0, 0, 0]])
        self.assertFalse(main.row_win(input_board, 1))

    def test_no_row_win_player_2(self):
        """Tests if no row win happened for player 2"""
        input_board = np.array([[2, 2, 0], [0, 0, 0], [0, 0, 0]])
        self.assertFalse(main.row_win(input_board, 1))

    def test_col_win_player_1(self):
        """Tests if player 1 won with the first column"""
        input_board = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
        self.assertTrue(main.col_win(input_board, 1))

    def test_col_win_player_2(self):
        """Tests if player 2 won with the first column"""
        input_board = np.array([[0, 2, 0], [0, 2, 0], [0, 2, 0]])
        self.assertTrue(main.col_win(input_board, 2))

    def test_no_col_win_player_1(self):
        """Tests if no column win happened for player 1"""
        input_board = np.array([[1, 0, 0], [0, 0, 0], [1, 0, 0]])
        self.assertFalse(main.col_win(input_board, 1))

    def test_no_col_win_player_2(self):
        """Tests if no column win happened for player 2"""
        input_board = np.array([[2, 0, 0], [2, 0, 0], [0, 0, 0]])
        self.assertFalse(main.col_win(input_board, 1))

    def test_diag_win_player_1(self):
        """Tests if player 1 won with the diagonal"""
        input_board = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertTrue(main.diag_win(input_board, 1))

    def test_diag_win_player_2(self):
        """Tests if player 2 won with the diagonal"""
        input_board = np.array([[0, 0, 2], [0, 2, 0], [2, 0, 0]])
        self.assertTrue(main.diag_win(input_board, 2))

    def test_no_diag_win_player_1(self):
        """Tests if no diagonal win happened for player 1"""
        input_board = np.array([[1, 0, 0], [0, 0, 0], [1, 0, 0]])
        self.assertFalse(main.diag_win(input_board, 1))

    def test_no_diag_win_player_2(self):
        """Tests if no diagonal win happened for player 2"""
        input_board = np.array([[2, 0, 0], [2, 0, 0], [0, 0, 0]])
        self.assertFalse(main.diag_win(input_board, 1))
