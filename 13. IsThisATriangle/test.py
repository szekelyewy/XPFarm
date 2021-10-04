import unittest as test

from main import is_triangle, if_int, if_positive


class TestStringMethods(test.TestCase):

    def test_IfTriangle(self):
        self.assertEqual(is_triangle(2, 3, 4), True)

    def test_IfNotTriangle(self):
        self.assertEqual(is_triangle(2, 2, 4), False)

    def test_IfInt(self):
        self.assertEqual(if_int(2), True)

    def test_IfNotInt(self):
        self.assertEqual(if_int('str'), False)

    def test_IfPositive(self):
        self.assertEqual(if_positive(2), True)

    def test_IfNotPositive(self):
        self.assertEqual(if_positive(-2), False)

    def test_IfZero(self):
        self.assertEqual(if_positive(0), False)


if __name__ == '__main__':
    test.main()
