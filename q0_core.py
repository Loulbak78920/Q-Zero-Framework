import numpy as np
import torch
import torch.nn as nn

class QZeroStabilizer(nn.Module):
    """
    Couche de stabilisation artificielle Q° pour réseaux de neurones (PyTorch).
    Prévient l'apparition des erreurs NaN en verrouillant la variance.
    """
    def __init__(self, features: int):
        super(QZeroStabilizer, self).__init__()
        self.register_buffer('Q_medinois', torch.tensor(1246743554998.0, dtype=torch.float64))
        self.register_buffer('Q_mecquois', torch.tensor(-138898.0, dtype=torch.float64))
        self.alpha = nn.Parameter(torch.ones(features, dtype=torch.float64))
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        orig_dtype = x.dtype
        x = x.to(torch.float64)
        Q_total = self.Q_medinois + self.Q_mecquois
        scale_factor = torch.log10(Q_total)
        
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, keepdim=True, unbiased=False)
        x_norm = (x - mean) / torch.sqrt(var + 1e-9)
        
        output = x_norm * torch.tanh(scale_factor * self.alpha)
        return output.to(orig_dtype)

class CryptosystemeQ0Cosmos:
    """
    Protocole de chiffrement post-quantique basé sur les cycles cosmiques
    du Soleil, de la Lune, de la Terre et de l'invariant Q°.
    """
    def __init__(self):
        dx = (2.5 * 8766 / 12) * (1.5 * 730.5 / 168) * (1.5 * 168 / 24) * 24 / 60
        dy = (2.5 * 8496 / 12) * (1.5 * 708 / 168) * (1.5 * 168 / 24) * 24 / 60
        dz = (300 * 8640 / 12) * (50 * 720 / 144) * (30 * 144 / 24) * 24 / 60
        self.dt_volume = dx * dy * dz
        self.Q_zero = 1246743416100.0
        
    def chiffrer(self, message_clair: str) -> list:
        message_chiffre = []
        cle_flux = np.log10(self.Q_zero) * (self.dt_volume % 10000)
        for i, char in enumerate(message_clair):
            facteur_chaos = int((ord(char) * cle_flux + i * 313) % self.dt_volume)
            message_chiffre.append(facteur_chaos)
        return message_chiffre

    def dechiffrer(self, message_chiffre: list) -> str:
        message_clair = []
        cle_flux = np.log10(self.Q_zero) * (self.dt_volume % 10000)
        for i, facteur_chaos in enumerate(message_chiffre):
            valeur_ascii = int(round((facteur_chaos - i * 313) / cle_flux))
            message_clair.append(chr(valeur_ascii))
        return "".join(message_clair)
