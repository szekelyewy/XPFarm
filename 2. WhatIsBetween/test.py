import unittest as test

from main import between, is_bigger


class TestStringMethods(test.TestCase):

    def test_ABiggerThanB(self):
        self.assertEqual(is_bigger(1, 2), True)

    def test_ASmallerThanB(self):
        self.assertEqual(is_bigger(2, 1), False)

    def test_AEqualsB(self):
        self.assertEqual(is_bigger(2, 2), False)

    def test_checkNumbersBetween(self):
        self.assertEqual(between(1, 4), [1, 2, 3, 4])

    def test_NoNumbersBetween(self):
        self.assertEqual(between(1, 2), [1, 2])


if __name__ == '__main__':
    test.main()
