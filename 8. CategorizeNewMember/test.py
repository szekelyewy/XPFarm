import unittest as test

from main import open_or_senior, check_if_older_than_55, check_if_handicap_greater_than_7, check_valid_handicap_range


class TestStringMethods(test.TestCase):

    def test_IfAllOpen(self):
        self.assertEqual(open_or_senior([(45, 12), (54, 13), (19, -2), (30, 10)]), ['Open', 'Open', 'Open', 'Open'])

    def test_IfAllSenior(self):
        self.assertEqual(open_or_senior([(56, 12), (55, 15), (70, 12), (100, 12)]), ['Senior', 'Senior', 'Senior', 'Senior'])

    def test_IfOpenAndSenior(self):
        self.assertEqual(open_or_senior([(45, 12), (56, 12), (19, -2), (67, 12)]), ['Open', 'Senior', 'Open', 'Senior'])

    def test_IfOlderThan55(self):
        self.assertEqual(check_if_older_than_55(65), True)

    def test_IfNotOlderThan55(self):
        self.assertEqual(check_if_older_than_55(45), False)

    def test_If55(self):
        self.assertEqual(check_if_older_than_55(55), True)

    def test_IfHandicapBiggerThan7(self):
        self.assertEqual(check_if_handicap_greater_than_7(8), True)

    def test_IfHandicapNumberSmallerThan7(self):
        self.assertEqual(check_if_handicap_greater_than_7(6), False)

    def test_IfHandicapNumber7(self):
        self.assertEqual(check_if_handicap_greater_than_7(7), False)

    def test_IfHandicapNumberInRange(self):
        self.assertEqual(check_valid_handicap_range(23), True)

    def test_IfHandicapNumberNotInRange(self):
        self.assertEqual(check_valid_handicap_range(-3), False)


if __name__ == '__main__':
    test.main()
