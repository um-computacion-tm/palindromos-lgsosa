from palindromo import palindrome, palindrome_1
from parameterized import parameterized, parameterized_class
import unittest

class TestPalindromo(unittest.TestCase):
    @parameterized.expand([
        ("neuquen", True),
        ("ama", True),
        ("ojo", True),
        ("Amo la paloma", True),
        ("Anita lava la tina", True)
    ])
    def test(self, palabra, resultado):
        self.assertEqual(palindrome(palabra),resultado)

if __name__ == '__main__':
    unittest.main()