import unittest as test

from main import checkIfString, greet


class TestStringMethods(test.TestCase):

    def test_IfString(self):
        self.assertEqual(checkIfString('string'), True)

    def test_IfNotString(self):
        self.assertEqual(checkIfString(20), False)

    def test_Greeting(self):
        self.assertEqual(greet('Shaun'), 'Hello, Shaun how are you doing today?')

    def test_GreetingWrong(self):
        self.assertNotEqual(greet('Shaun'), 'Hello, NotShaun how are you doing today?')



if __name__ == '__main__':
    test.main()
