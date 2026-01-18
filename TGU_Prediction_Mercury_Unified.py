
import matplotlib.pyplot as plt

# Dados orbitais de Mercúrio
a = 0.387  # Semieixo maior (UA)
e = 0.206  # Excentricidade
T = 87.97  # Período orbital (dias)

# Precessão prevista pela Relatividade Geral (RG) para Mercúrio
precessao_RG = 42.98  # arcseg/século (valor observado)

# Constante unificada da TGU (obtida por regressão nos dados anteriores)
k = 0.0881

# Cálculo do fator de correção alpha pela fórmula unificada da TGU
alpha_TGU = 1 + k * (e / a)

# Precessão TGU = alpha * precessão_RG
precessao_TGU = alpha_TGU * precessao_RG

# Correção informacional = diferença entre TGU e RG
correcao = precessao_TGU - precessao_RG

# Exibir resultados
print("===== TGU Precession Prediction for Mercury =====")
print(f"Semieixo maior (a): {a} UA")
print(f"Excentricidade (e): {e}")
print(f"Fator de Correção α (TGU): {alpha_TGU:.4f}")
print(f"Precessão RG: {precessao_RG:.4f} arcseg/século")
print(f"Precessão TGU: {precessao_TGU:.4f} arcseg/século")
print(f"Correção TGU - RG: {correcao:.4f} arcseg/século")

# Gráfico comparativo
labels = ['RG (Einstein)', 'TGU (Unificada)']
values = [precessao_RG, precessao_TGU]

plt.figure(figsize=(8, 5))
bars = plt.bar(labels, values, color=['gray', 'orange'])
plt.ylabel("Precessão (arcseg/século)")
plt.title("Precessão do Periélio de Mercúrio — RG vs TGU")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.text(0, precessao_RG + 0.3, f"{precessao_RG:.2f}", ha='center')
plt.text(1, precessao_TGU + 0.3, f"{precessao_TGU:.2f}", ha='center')
plt.tight_layout()
plt.savefig("TGU_Prediction_Mercury_Unified.png")
plt.show()
