"""
TGU MASTER - Precessão do Periélio da Terra
Author: Henry Matuchaki (@MatuchakiSilva)
Versão Refinada: Inclui fator de resistência à coerência para convergência com GR
"""

import matplotlib.pyplot as plt
import numpy as np

# Constantes MASTER TGU
K = 0.0881                  # Matuchaki Parameter
N = 12                      # Expoente harmônico de coerência
RS_INFORMATIONAL = 0.02391625  # Raio de coerência solar (AU)

# Parâmetros da Terra
e = 0.0167                  # Excentricidade
a = 1.000                   # Semi-eixo maior (AU)
precessao_rg = 3.84         # Precessão GR (arcsec/século)

# Cálculo MASTER TGU
alpha = 1 + K * (e / a)
epsilon = 1.0 + (RS_INFORMATIONAL / a) ** 2
coherence_factor = epsilon ** (-N)
precessao_tgu = precessao_rg * alpha * coherence_factor

print(f"Fator alpha (ganho informacional): {alpha:.6f}")
print(f"Fator de resistência à coerência (ε^{-N}): {coherence_factor:.6f}")
print(f"Precessão TGU refinada (arcsec/século): {precessao_tgu:.6f}")
print(f"Convergência com GR: {precessao_tgu / precessao_rg * 100:.2f}%")

# Plotagem comparativa
labels = ['Relatividade Geral', 'TGU (Alpha sozinho)', 'TGU MASTER (Refinada)']
valores = [precessao_rg, precessao_rg * alpha, precessao_tgu]

plt.figure(figsize=(10, 6))
plt.bar(labels, valores, color=['gray', 'lightblue', 'darkblue'])
plt.title('Precessão do Periélio da Terra: RG vs. TGU (Alpha) vs. TGU MASTER')
plt.ylabel('Precessão (arcsec/século)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Linha de referência GR
plt.axhline(precessao_rg, color='gray', linestyle='--', alpha=0.7, label='Valor RG')

plt.legend()
plt.tight_layout()
plt.savefig("TGU_Prediction_Earth_Precession_MASTER.png")
plt.show()
