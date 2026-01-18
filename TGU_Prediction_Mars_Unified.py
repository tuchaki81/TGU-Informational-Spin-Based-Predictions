
import math
import matplotlib.pyplot as plt

# Constantes físicas e parâmetros orbitais de Marte
a = 1.523679  # AU
e = 0.0934
k = 0.088  # Constante de coerência informacional da TGU

# Precessão da Relatividade Geral para Marte (valor base conhecido)
precessao_gr = 1.35  # arcseg/century

# Cálculo do fator alfa usando a fórmula unificada
alpha = 1 + k * (e / a)

# Correção TGU e precessão total
correcao_tgu = (alpha - 1) * precessao_gr
precessao_total = precessao_gr + correcao_tgu

# Impressão dos resultados
print(f"Alpha (TGU): {alpha:.6f}")
print(f"Correção TGU: {correcao_tgu:.6f} arcseg/século")
print(f"Precessão Total (TGU): {precessao_total:.6f} arcseg/século")

# Gráfico comparativo
labels = ['GR Only', 'TGU Correction', 'Total (TGU)']
values = [precessao_gr, correcao_tgu, precessao_total]
colors = ['gray', 'orange', 'blue']

plt.figure(figsize=(8, 5))
bars = plt.bar(labels, values, color=colors)
plt.title("TGU Unified Prediction vs GR — Mars")
plt.ylabel("Precessão (arcseg/século)")

# Adiciona os valores no topo das barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.01, f'{yval:.3f}', ha='center', va='bottom')

plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("/mnt/data/TGU_Prediction_Mars_Unified.py.png")
plt.show()
