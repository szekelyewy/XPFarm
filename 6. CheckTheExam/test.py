import unittest as test

from main import check_exam, check_input


class TestStringMethods(test.TestCase):

    def test_ExamResults(self):
        self.assertEqual(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6)

    def test_AnswerLowerThanZero(self):
        self.assertEqual(check_exam(["a", "a", "b", "b"], ["b", "", "", ""]), 0)

    def test_CorrectAnswer(self):
        self.assertEqual(check_exam(["a", "a", "b", "b"], ["a", "", "", ""]), 4)

    def test_emptyInput(self):
        self.assertEqual(check_input(""), False)

    def test_input(self):
        self.assertEqual(check_input("a"), True)


if __name__ == '__main__':
    test.main()
