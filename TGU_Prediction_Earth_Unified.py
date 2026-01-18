
import matplotlib.pyplot as plt

# Constantes físicas da Terra
e = 0.0167  # Excentricidade
a = 1.000   # Unidade Astronômica (UA)
precessao_rg = 3.84  # Valor da Relatividade Geral (arcseg/século)
k = 0.0881  # Constante da TGU

# Cálculo do fator alpha pela fórmula unificada da TGU
alpha_tgu = 1 + k * (e / a)
precessao_tgu = precessao_rg * alpha_tgu

print(f"Fator alpha (TGU): {alpha_tgu:.6f}")
print(f"Precessão TGU (arcseg/século): {precessao_tgu:.6f}")

# Plotagem comparativa
labels = ['Relatividade Geral', 'TGU (Unificada)']
valores = [precessao_rg, precessao_tgu]

plt.figure(figsize=(8, 5))
plt.bar(labels, valores, color=['gray', 'blue'])
plt.title('Precessão do Periélio da Terra segundo RG e TGU')
plt.ylabel('Precessão (arcseg/século)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("TGU_Prediction_Earth_Precession.png")
plt.show()
