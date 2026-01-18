
"""
TGU - Unified Alpha Prediction for Perihelion Precession
Asteroid: Icarus
"""

import matplotlib.pyplot as plt

# Constantes
k = 0.0881  # Constante de coerência unificada da TGU
e = 0.827   # Excentricidade de Ícarus
a = 1.077   # Semieixo maior em Unidades Astronômicas (UA)

# Precessão observada (Relatividade Geral) em arcseg/século
precession_rg = 10.05

# Cálculo do fator alpha com base na fórmula unificada da TGU
alpha = 1 + k * (e / a)

# Precessão prevista pela TGU
precession_tgu = alpha * precession_rg

# Impressão dos resultados
print(f"Fator α calculado pela TGU: {alpha:.4f}")
print(f"Precessão (RG): {precession_rg:.2f} arcseg/século")
print(f"Precessão (TGU): {precession_tgu:.2f} arcseg/século")

# Plotagem comparativa
labels = ['Relativity (GR)', 'TGU Prediction']
values = [precession_rg, precession_tgu]

plt.figure(figsize=(6, 4))
bars = plt.bar(labels, values, color=['gray', 'purple'])
plt.title('Perihelion Precession of Icarus')
plt.ylabel('arcsec / century')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.1, f'{yval:.2f}', ha='center', va='bottom')
plt.tight_layout()
plt.savefig("/mnt/data/TGU_Prediction_Icarus_Precession.png")
plt.close()
