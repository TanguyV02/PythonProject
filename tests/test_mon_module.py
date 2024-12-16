import unittest
from src.mon_module import ajouter

class TestMonModule(unittest.TestCase):
    def test_ajouter_nombres(self):
        """Teste l'addition de deux nombres simples."""
        self.assertEqual(ajouter(2, 3), 5)
        self.assertEqual(ajouter(-1, 1), 0)
        self.assertEqual(ajouter(2.5, 3.5), 6.0)

    def test_ajouter_listes(self):
        """Teste l'addition de deux listes ou tuples."""
        self.assertEqual(ajouter([1, 2], [3, 4]), [4, 6])
        self.assertEqual(ajouter((1, 2), (3, 4)), (4, 6))

    def test_erreurs(self):
        """Teste les cas qui doivent lever une erreur."""
        with self.assertRaises(ValueError):
            ajouter([1, 2], [3])  # Listes de tailles différentes
        with self.assertRaises(ValueError):
            ajouter(2, [3])  # Types incompatibles
        with self.assertRaises(ValueError):
            ajouter("a", "b")  # Types non pris en charge

if __name__ == '__main__':
    unittest.main()
