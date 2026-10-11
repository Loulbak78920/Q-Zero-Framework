import unittest

import torch

from q0_master_framework import QZeroFrameworkLinguistique, QZeroNormalization


class TestValidationSystemeQ0(unittest.TestCase):
    def setUp(self):
        """Initialise les composants du framework pour chaque test."""
        self.framework = QZeroFrameworkLinguistique()
        self.d_model = 64
        self.couche_norm = QZeroNormalization(d_model=self.d_model)

    def test_calcul_point_fixe_eau_reel(self):
        resultat = self.framework.resoudre_systeme(
            "Réseau Eau", "מים", 399134
        )
        self.assertEqual(resultat["q_zero"], 3052513797449)

    def test_non_generation_nan_sur_echantillon(self):
        tenseur_stress = torch.randn(2, 5, self.d_model) * 1e12
        sortie = self.couche_norm(tenseur_stress)

        contient_nan = torch.isnan(sortie).any().item()
        self.assertFalse(
            contient_nan, "La couche a généré une valeur aberrante NaN."
        )
        self.assertEqual(sortie.shape, (2, 5, self.d_model))


if __name__ == "__main__":
    unittest.main()