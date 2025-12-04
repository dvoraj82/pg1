from muj_modul import fibonaci
import unittest


class TestMujModul(unittest.TestCase):
    def test_fibonaci(self):
        vysledek = fibonaci(2)
        self.assertEqual(vysledek, [1, 1, 2])

        vysledek = fibonaci(10)
        self.assertEqual(vysledek, [1, 1, 2, 3])

    def test_secti(self):
        self.assertEqual(2 + 2, 4)