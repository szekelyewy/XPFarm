import unittest as test

from main import check_type, check_vowel_length, vowel_change, check_vowel_list


class TestStringMethods(test.TestCase):

    def test_IfString(self):
        self.assertEqual(check_type('string'), True)

    def test_IfNotString(self):
        self.assertEqual(check_type(2), False)

    def test_IfVowelOnlyOneLetter(self):
        self.assertEqual(check_vowel_length('s'), True)

    def test_IfVowelNotOnlyOneLetter(self):
        self.assertEqual(check_vowel_length('ss'), False)

    def test_IfVowelGiven(self):
        self.assertEqual(check_vowel_list('a'), True)

    def test_IfNotVowelGiven(self):
        self.assertEqual(check_vowel_list('s'), False)

    def test_VowelChange(self):
        self.assertEqual(vowel_change("hannah hannah bo-bannah banana fanna fo-fannah fee, fy, mo-mannah. hannah!", 'i'), 'hinnih hinnih bi-binnih binini finni fi-finnih fii, fy, mi-minnih. hinnih!')

    def test_VowelChange2(self):
        self.assertEqual(vowel_change('adira wants to go to the park', 'o'), 'odoro wonts to go to tho pork')


if __name__ == '__main__':
    test.main()
