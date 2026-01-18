"""
TGU MASTER - Unified Prediction for Perihelion Precession
Planet: Venus (Refined with Coherence Resistance Factor)
Author: Henry Matuchaki (@MatuchakiSilva)
"""

import matplotlib.pyplot as plt
import numpy as np

# MASTER TGU Constants
K = 0.0881                  # Matuchaki Parameter
N = 12                      # Harmonic Coherence Exponent
RS_INFORMATIONAL = 0.02391625  # Solar Coherence Radius (AU)

# Orbital Parameters for Venus
e_venus = 0.0068            # Eccentricity
a_venus = 0.723             # Semi-major axis (AU)
precessao_rg = 8.6247       # GR Reference (arcsec/century)

# MASTER TGU Calculations
alpha = 1 + K * (e_venus / a_venus)     # Informational gain
epsilon = 1.0 + (RS_INFORMATIONAL / a_venus) ** 2
coherence_factor = epsilon ** (-N)      # Resistance factor
precessao_tgu = precessao_rg * alpha * coherence_factor

# Correction breakdown
correcao = precessao_tgu - precessao_rg

# Output
print("=== TGU MASTER Precessão de Vênus ===")
print("-" * 40)
print(f"Excentricidade (e): {e_venus}")
print(f"Distância média (a): {a_venus} AU")
print(f"Fator de Ganho α (TGU): {alpha:.8f}")
print(f"Fator de Resistência à Coerência (ε^{-N}): {coherence_factor:.8f}")
print(f"Precessão RG: {precessao_rg:.6f} arcseg/century")
print(f"Precessão TGU MASTER: {precessao_tgu:.6f} arcseg/century")
print(f"Correção TGU: {correcao:.6f} arcseg/century")
print(f"Convergência com GR: {precessao_tgu / precessao_rg * 100:.2f}%")

# Visualização comparativa
labels = ['Relatividade Geral', 'TGU (Alpha only)', 'TGU MASTER (Refinada)']
values = [precessao_rg, precessao_rg * alpha, precessao_tgu]
colors = ['gray', 'lightblue', 'darkblue']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, values, color=colors)
ax.set_ylabel("Precessão (arcseg/century)")
ax.set_title("Precessão de Vênus: RG vs. TGU vs. TGU MASTER")
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Adiciona valores no topo das barras
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.02, f"{yval:.4f}", 
            ha='center', va='bottom')

# Linha de referência GR
ax.axhline(precessao_rg, color='gray', linestyle='--', alpha=0.7, label='Valor RG')

ax.legend()
plt.tight_layout()
plt.savefig("TGU_Prediction_Venus_MASTER.png")
plt.show()
