import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def tests(self):
        self.assertEqual(english_to_french("Hello"), 'Bonjour')
        self.assertNotEqual(english_to_french("Hello"), 'Hello')

class TestFrenchToEnglish(unittest.TestCase):
    def tests(self):
        self.assertEqual(french_to_english("Bonjour"), 'Hello')
        self.assertNotEqual(french_to_english("Bonjour"), 'Bonjour')

if __name__ == '__main__':
    unittest.main()
