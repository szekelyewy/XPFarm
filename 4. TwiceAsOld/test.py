import unittest as test

from main import is_bigger, twice_as_old


class TestStringMethods(test.TestCase):

    def test_ABiggerThanB(self):
        self.assertEqual(is_bigger(1, 2), True)

    def test_ASmallerThanB(self):
        self.assertEqual(is_bigger(2, 1), False)

    def test_AEqualsB(self):
        self.assertEqual(is_bigger(2, 2), False)

    def test_RightCalculation(self):
        self.assertEqual(twice_as_old(36, 7), 22)


if __name__ == '__main__':
    test.main()
