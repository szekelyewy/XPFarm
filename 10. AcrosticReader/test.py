import unittest as test

from main import read_out, check_data_type


class TestStringMethods(test.TestCase):

    def test_RandomWord(self):
        self.assertEqual(read_out(['Jolly', 'Amazing', 'Courteous', 'Keen']), 'JACK')

    def test_IfStringType(self):
        self.assertEqual(check_data_type('string'), True)

    def test_IfNotStringType(self):
        self.assertEqual(check_data_type(4), False)


if __name__ == '__main__':
    test.main()
