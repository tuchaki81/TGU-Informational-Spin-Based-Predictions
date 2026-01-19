import numpy as np
import matplotlib.pyplot as plt

# --- CONFIGURAÇÕES DA SIMULAÇÃO ---
# Her-CrB GW: ~3000 Mpc de extensão, Redshift z ~ 2.0
DISTANCIA_GPC = 3.0  # Giga-parsecs
GRID_RES = 100       # Resolução da malha

# --- 1. MODELAGEM DO CAMPO INFORMACIONAL (I) ---
def gerar_campo_informacional(x, y):
    """
    Simula uma 'Bacia de Coerência' filamentar.
    Na TGU, a matéria se acumula onde a coerência informacional é maior.
    """
    # Criação de um filamento curvo (analogia à Grande Muralha)
    # y = 0.2 * sin(2x) define a 'espinha dorsal' da estrutura
    filament = np.exp(-(y - 0.2 * np.sin(2 * x))**2 / 0.05)
    
    # Ruído de fundo (coerência cósmica residual)
    ruido = 0.1 * np.random.normal(0, 0.1, x.shape)
    
    return filament + ruido

# Gerar malha de coordenadas
x_range = np.linspace(-2, 2, GRID_RES)
y_range = np.linspace(-2, 2, GRID_RES)
X, Y = np.meshgrid(x_range, y_range)

# Calcular o Campo I
campo_I = gerar_campo_informacional(X, Y)

# --- 2. CÁLCULO DOS GRADIENTES (FORÇA TGU) ---
# Segundo a TGU, a força que organiza a estrutura é o gradiente da coerência
dy, dx = np.gradient(campo_I)
magnitude_gradiente = np.sqrt(dx**2 + dy**2)

# --- 3. COMPARAÇÃO EVOLUTIVA (TGU vs CDM) ---
z_escala = np.linspace(0, 15, 100) # Redshift de 0 a 15

# Modelo Padrão (Lambda-CDM): Crescimento hierárquico lento
tamanho_cdm = 1.0 / (1 + z_escala)

# Modelo TGU: Coerência permite estruturas grandes muito cedo (z > 10)
# A função exponencial representa a estabilização rápida da fase informacional
tamanho_tgu = 0.8 * np.exp(-0.05 * z_escala) + 0.2

# --- 4. VISUALIZAÇÃO ---
def plotar_resultados():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Gráfico do Campo de Coerência
    cont = ax1.contourf(X, Y, campo_I, cmap='inferno')
    ax1.set_title('Campo de Coerência Informacional (I)\nSimulação Her-CrB GW')
    plt.colorbar(cont, ax=ax1, label='Densidade de Coerência')
    
    # Gráfico da Linha do Tempo
    ax2.plot(z_escala, tamanho_cdm, 'r--', label='Modelo Padrão (ΛCDM)')
    ax2.plot(z_escala, tamanho_tgu, 'b-', label='TGU (Coerência)')
    ax2.axvline(x=2.0, color='k', linestyle=':', label='Her-CrB GW (z~2)')
    ax2.invert_xaxis() # Redshift maior = passado
    ax2.set_title('Evolução do Tamanho das Estruturas')
    ax2.set_xlabel('Redshift (z)')
    ax2.set_ylabel('Escala da Estrutura (Normalizada)')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()

# Executar visualização
if __name__ == "__main__":
    plotar_resultados()
    print(f"Gradiente Médio de Coerência no Filamento: {np.mean(magnitude_gradiente):.4f}")