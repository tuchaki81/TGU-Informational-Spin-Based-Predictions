"""
TGU MASTER - Unified Alpha Prediction for Perihelion Precession
Asteroid: Icarus (Refined with Coherence Resistance Factor)
Author: Henry Matuchaki (@MatuchakiSilva)
"""

import matplotlib.pyplot as plt
import numpy as np

# MASTER TGU Constants
K = 0.0881                  # Matuchaki Parameter
N = 12                      # Harmonic Coherence Exponent
RS_INFORMATIONAL = 0.02391625  # Solar Coherence Radius (AU)

# Orbital Parameters for Icarus
e = 0.827                   # Eccentricity
a = 1.077                   # Semi-major axis (AU)
precession_rg = 10.05       # GR Reference (arcsec/century)

# MASTER TGU Calculations
alpha = 1 + K * (e / a)     # Informational gain
epsilon = 1.0 + (RS_INFORMATIONAL / a) ** 2
coherence_factor = epsilon ** (-N)  # Resistance factor
precession_tgu = precession_rg * alpha * coherence_factor

# Output
print("TGU MASTER ANALYSIS – ICARUS")
print("-" * 40)
print(f"Informational Gain (Alpha):          {alpha:.6f}")
print(f"Coherence Resistance (ε^{-N}):       {coherence_factor:.6f}")
print(f"Final TGU Precession:                {precession_tgu:.2f} arcsec/century")
print(f"Convergence with GR:                 {precession_tgu / precession_rg * 100:.2f}%")

# Comparative Bar Plot
labels = ['Relativity (GR)', 'TGU (Alpha only)', 'TGU MASTER (Refined)']
values = [precession_rg, precession_rg * alpha, precession_tgu]
colors = ['gray', 'lightblue', 'darkblue']

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, values, color=colors)
plt.title('Perihelion Precession of Icarus: RG vs. TGU vs. TGU MASTER', fontsize=14)
plt.ylabel('Precession (arcsec/century)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.1, f'{yval:.2f}', 
             ha='center', va='bottom', fontsize=10)

# Reference line for GR
plt.axhline(precession_rg, color='gray', linestyle='--', alpha=0.7, label='GR Baseline')

plt.legend()
plt.tight_layout()
plt.savefig("TGU_Prediction_Icarus_Precession_MASTER.png")
plt.show()
