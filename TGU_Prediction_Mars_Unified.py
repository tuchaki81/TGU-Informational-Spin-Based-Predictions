"""
TGU MASTER - Unified Prediction for Perihelion Precession
Planet: Mars (Refined with Coherence Resistance Factor)
Author: Henry Matuchaki (@MatuchakiSilva)
"""

import matplotlib.pyplot as plt
import numpy as np

# MASTER TGU Constants
K = 0.0881                  # Matuchaki Parameter
N = 12                      # Harmonic Coherence Exponent
RS_INFORMATIONAL = 0.02391625  # Solar Coherence Radius (AU)

# Orbital Parameters for Mars
a = 1.523679                # Semi-major axis (AU)
e = 0.0934                  # Eccentricity
precessao_gr = 1.35         # GR Reference (arcsec/century)

# MASTER TGU Calculations
alpha = 1 + K * (e / a)     # Informational gain
epsilon = 1.0 + (RS_INFORMATIONAL / a) ** 2
coherence_factor = epsilon ** (-N)  # Resistance factor
precessao_tgu = precessao_gr * alpha * coherence_factor

# Additional breakdown
correcao_tgu = precessao_tgu - precessao_gr

# Output
print("TGU MASTER ANALYSIS – MARS")
print("-" * 40)
print(f"Informational Gain (Alpha):          {alpha:.6f}")
print(f"Coherence Resistance (ε^{-N}):       {coherence_factor:.6f}")
print(f"Correction from GR:                  {correcao_tgu:.6f} arcsec/century")
print(f"Final TGU Precession:                {precessao_tgu:.6f} arcsec/century")
print(f"Convergence with GR:                 {precessao_tgu / precessao_gr * 100:.2f}%")

# Comparative Bar Plot
labels = ['GR Only', 'TGU Gain Only', 'TGU MASTER (Refined)']
values = [precessao_gr, precessao_gr * alpha, precessao_tgu]
colors = ['gray', 'lightblue', 'darkblue']

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, values, color=colors)
plt.title('Perihelion Precession of Mars: GR vs. TGU vs. TGU MASTER', fontsize=14)
plt.ylabel('Precession (arcsec/century)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.01, f'{yval:.3f}', 
             ha='center', va='bottom', fontsize=10)

# Reference line for GR
plt.axhline(precessao_gr, color='gray', linestyle='--', alpha=0.7, label='GR Baseline')

plt.legend()
plt.tight_layout()
plt.savefig("TGU_Prediction_Mars_MASTER.png")
plt.show()
