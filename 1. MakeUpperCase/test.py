import unittest as test

from main import make_upper_case, if_string


class TestStringMethods(test.TestCase):

    def test_ifString(self):
        self.assertEqual(if_string('string'), True)

    def test_ifNotSting(self):
        self.assertEqual(if_string(1), False)

    def test_ToUpperCase(self):
        self.assertEqual(make_upper_case("string"), "STRING")


if __name__ == '__main__':
    test.main()
