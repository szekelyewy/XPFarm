import unittest as test

from main import square_digits, check_data_type


class TestStringMethods(test.TestCase):

    def test_IfZero(self):
        self.assertEqual(square_digits(0), 0)

    def test_RandomNumber(self):
        self.assertEqual(square_digits(9119), 811181)

    def test_IfIntType(self):
        self.assertEqual(check_data_type(7), True)

    def test_IfNotIntType(self):
        self.assertEqual(check_data_type('7'), False)


if __name__ == '__main__':
    test.main()