import numpy as np
import matplotlib.pyplot as plt

# ================================================
# Teoria Unificada do Spin Informacional (TGU)
# Precessão de Vênus usando fórmula unificada
# ================================================

# Constantes físicas e astronômicas
AU = 1.496e11  # Unidade astronômica em metros
e_venus = 0.0068  # Excentricidade orbital de Vênus
a_venus = 0.723  # Distância média do Sol em AU
precessao_RG = 8.6247  # Precessão predita pela Relatividade Geral para Vênus (arcseg/century)

# Fórmula unificada para o fator α:
# α = 1 + k * (e / a)
k = 0.088
alpha_unificado = 1 + k * (e_venus / a_venus)

# Correção TGU aplicada à precessão da Relatividade Geral
precessao_TGU = precessao_RG * alpha_unificado
correcao = precessao_TGU - precessao_RG

# Impressão dos resultados
print("=== Precessão de Vênus segundo a TGU ===")
print(f"Excentricidade (e): {e_venus}")
print(f"Distância média (a): {a_venus} AU")
print(f"Fator α unificado: {alpha_unificado:.8f}")
print(f"Precessão RG: {precessao_RG:.6f} arcseg/century")
print(f"Precessão TGU: {precessao_TGU:.6f} arcseg/century")
print(f"Correção TGU: {correcao:.6f} arcseg/century")

# Visualização
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(["Relatividade Geral", "TGU (Unificada)"], [precessao_RG, precessao_TGU], color=["gray", "orange"])
ax.set_ylabel("Precessão (arcseg/century)")
ax.set_title("Precessão de Vênus: RG vs TGU (Fórmula Unificada)")
for i, val in enumerate([precessao_RG, precessao_TGU]):
    ax.text(i, val + 0.02, f"{val:.4f}", ha='center', va='bottom')
plt.tight_layout()
plt.savefig("TGU_Prediction_Venus_Unified.png")
plt.show()
