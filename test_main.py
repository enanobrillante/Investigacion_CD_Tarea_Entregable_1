import unittest
from main import es_palindromo, es_primo, es_mayor_de_edad


class TestFunciones(unittest.TestCase):

    def test_es_palindromo(self):
        self.assertTrue(es_palindromo("radar"))


    def test_es_primo(self):
        self.assertTrue(es_primo(23))

    def test_es_mayor_de_edad(self):
        self.assertTrue(es_mayor_de_edad(18))
        

if __name__ == "__main__":
    unittest.main()