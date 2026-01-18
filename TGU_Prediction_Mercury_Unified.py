"""
TGU MASTER - Unified Prediction for Perihelion Precession
Planet: Mercury (Refined with Coherence Resistance Factor)
Author: Henry Matuchaki (@MatuchakiSilva)
"""

import matplotlib.pyplot as plt
import numpy as np

# MASTER TGU Constants
K = 0.0881                  # Matuchaki Parameter
N = 12                      # Harmonic Coherence Exponent
RS_INFORMATIONAL = 0.02391625  # Solar Coherence Radius (AU)

# Orbital Parameters for Mercury
a = 0.387                   # Semi-major axis (AU)
e = 0.206                   # Eccentricity
T = 87.97                   # Orbital period (days, unused here)
precessao_rg = 42.98        # GR Reference (arcsec/century)

# MASTER TGU Calculations
alpha = 1 + K * (e / a)     # Informational gain
epsilon = 1.0 + (RS_INFORMATIONAL / a) ** 2
coherence_factor = epsilon ** (-N)  # Resistance factor
precessao_tgu = precessao_rg * alpha * coherence_factor

# Correction breakdown
correcao = precessao_tgu - precessao_rg

# Output
print("===== TGU MASTER Precession Prediction for Mercury =====")
print(f"Semieixo maior (a): {a} UA")
print(f"Excentricidade (e): {e}")
print(f"Fator de Ganho α (TGU): {alpha:.4f}")
print(f"Fator de Resistência à Coerência (ε^{-N}): {coherence_factor:.4f}")
print(f"Precessão RG: {precessao_rg:.4f} arcseg/século")
print(f"Precessão TGU MASTER: {precessao_tgu:.4f} arcseg/século")
print(f"Correção TGU - RG: {correcao:.4f} arcseg/século")
print(f"Convergência com GR: {precessao_tgu / precessao_rg * 100:.2f}%")

# Comparative Bar Plot
labels = ['RG (Einstein)', 'TGU (Alpha only)', 'TGU MASTER (Refined)']
values = [precessao_rg, precessao_rg * alpha, precessao_tgu]
colors = ['gray', 'lightblue', 'darkblue']

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, values, color=colors)
plt.ylabel("Precessão (arcseg/século)", fontsize=12)
plt.title("Precessão do Periélio de Mercúrio — RG vs. TGU vs. TGU MASTER", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Add value labels on bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.3, f"{yval:.2f}", 
             ha='center', va='bottom', fontsize=10)

# Reference line for GR
plt.axhline(precessao_rg, color='gray', linestyle='--', alpha=0.7, label='Valor RG')

plt.legend()
plt.tight_layout()
plt.savefig("TGU_Prediction_Mercury_MASTER.png")
plt.show()
