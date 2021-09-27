import unittest as test

from main import check_if_string, str_count


class TestStringMethods(test.TestCase):

    def test_IfString(self):
        self.assertEqual(check_if_string('str'), True)

    def test_IfNotString(self):
        self.assertEqual(check_if_string(1), False)

    def test_Count(self):
        self.assertEqual(str_count('hello', 'l'), 2)

    def test_ZeroCount(self):
        self.assertEqual(str_count('hello', 't'), 0)


if __name__ == '__main__':
    test.main()
