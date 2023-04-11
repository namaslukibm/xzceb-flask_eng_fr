import unittest
import sys
sys.path.insert(0, '.')

from machinetranslation.translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):

    def test_englishToFrench(self):
        # test "Hello" --> "Bonjour"
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        # test "Hats" --> "Chapeaux"
        self.assertEqual(englishToFrench('Hats'), 'Chapeaux')
        # test null input, should raise a TypeError
        with self.assertRaises(TypeError):
            englishToFrench()

    def test_frenchToEnglish(self):
        # test "Bonjour" --> Hello
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        # test "Chapeaux" --> "Hats"
        self.assertEqual(frenchToEnglish('Chapeaux'), 'Hats')
        # test null input, should raise a TypeError
        with self.assertRaises(TypeError):
            frenchToEnglish()


if __name__ == '__main__':
    unittest.main()
