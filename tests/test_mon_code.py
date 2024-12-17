import unittest
import numpy as np
from src.mon_code import generate_signal, add_noise, compute_fourier_transform

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

class TestMonCode(unittest.TestCase):
    def test_generate_signal(self):
        """Test la génération d'un signal sinusoïdal."""
        t, signal = generate_signal(freq=10, sampling_rate=100, duration=1)
        self.assertEqual(len(t), 100)  # Vérifie le nombre d'échantillons
        self.assertTrue(np.allclose(signal, np.sin(2 * np.pi * 10 * t)))  # Vérifie le contenu

    def test_add_noise(self):
        """Test l'ajout de bruit à un signal."""
        _, signal = generate_signal()
        noisy_signal = add_noise(signal, noise_level=0.5)
        self.assertEqual(len(signal), len(noisy_signal))  # Même longueur
        self.assertNotEqual(np.sum(signal), np.sum(noisy_signal))  # Vérifie que du bruit a été ajouté

    def test_compute_fourier_transform(self):
        """Test le calcul de la transformée de Fourier."""
        _, signal = generate_signal(freq=5, sampling_rate=100, duration=1)
        fft_freq, fft_magnitude = compute_fourier_transform(signal, sampling_rate=100)
        self.assertEqual(len(fft_freq), len(signal))  # Longueur correcte
        self.assertTrue(np.argmax(fft_magnitude[:len(fft_freq)//2]) == 5)  # Pic à la bonne fréquence

if __name__ == '__main__':
    unittest.main()
