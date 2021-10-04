import unittest as test

from main import sum_cubes, if_positive, if_int, cubed_number


class TestStringMethods(test.TestCase):

    def test_IfPositive(self):
        self.assertEqual(if_positive(5), True)

    def test_IfNegative(self):
        self.assertEqual(if_positive(-1), False)

    def test_IfZero(self):
        self.assertEqual(if_positive(0), False)

    def test_IfInt(self):
        self.assertEqual(if_int(1), True)

    def test_IfNotInt(self):
        self.assertEqual(if_int('str'), False)

    def test_squareNumber1(self):
        self.assertEqual(cubed_number(2), 8)

    def test_squareNumber2(self):
        self.assertEqual(cubed_number(5), 125)

    def test_SumCubes(self):
        self.assertEqual(sum_cubes(3), 36)

    def test_SumCubes2(self):
        self.assertEqual(sum_cubes(4), 100)


if __name__ == '__main__':
    test.main()
