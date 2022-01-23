import unittest

from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Farewell"), "Adieu")
        self.assertEqual(english_to_french("What time is it?"), "Quelle heure est-il?")

    def test1none(self):
        self.assertRaises(ValueError, english_to_french, None)


class TestfrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Adieu"), "Goodbye")
        self.assertEqual(french_to_english("Il est tard."), "It's late.")

    def test2none(self):

        self.assertRaises(ValueError, french_to_english, None)

if __name__ == "__main__":

    unittest.main()
    