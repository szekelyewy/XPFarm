import unittest

import main


class TestClass(unittest.TestCase):

    def test_init_board(self):
        self.assertEqual([[0, 0, 0], [0, 0, 0], [0, 0, 0]], main.init_board())

    def test_init_board_negative(self):
        self.assertNotEqual([[1, 0, 0], [0, 0, 0], [0, 0, 0]], main.init_board())
