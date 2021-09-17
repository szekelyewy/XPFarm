import unittest as test

from main import check


class TestStringMethods(test.TestCase):

    def test_ifIntIsIn(self):
        self.assertEqual(check([11, 22, 33], 33), True)

    def test_ifIntIsNotIn(self):
        self.assertEqual(check([11, 22, 33], 44), False)

    def test_ifStringIsIn(self):
        self.assertEqual(check(['11', '22', '33'], '33'), True)

    def test_ifStringIsNotIn(self):
        self.assertEqual(check(['11', '22', '33'], '44'), False)


if __name__ == '__main__':
    test.main()
