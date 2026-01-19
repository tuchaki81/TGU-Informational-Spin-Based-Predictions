import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# CONSTANTES FÍSICAS
# ============================================================
G = 6.67430e-11          # Constante gravitacional (m^3 kg^-1 s^-2)
M_SUN = 1.98847e30       # Massa solar (kg)
KPC = 3.085677581e19     # kiloparsec em metros
KM_S = 1000.0            # Conversão m/s → km/s

# ============================================================
# PARÂMETROS TGU (Matuchaki, 2025)
# ============================================================
K_TGU = 0.0881           # Parâmetro de eficiência de coerência
N_COHERENCE = 12         # Expoente harmônico
R_S_INFO = 0.0           # Em galáxias pode ser negligenciado (≈ 0)

# ============================================================
# MODELOS AUXILIARES
# ============================================================

def massa_disco_exponencial(r_kpc, M_disk, R_d):
    """
    Massa cumulativa de um disco exponencial:
    M(r) = M_disk * [1 - (1 + r/R_d) * exp(-r/R_d)]
    
    r_kpc : raio (kpc)
    M_disk : massa total do disco (em massas solares)
    R_d : raio de escala do disco (kpc)
    """
    return M_disk * (1.0 - (1.0 + r_kpc / R_d) * np.exp(-r_kpc / R_d))


def fator_coerencia(r_kpc):
    """
    Fator de resistência harmônica ε(r)^(-n).
    Para galáxias, o termo rs/r é desprezível.
    """
    epsilon = 1.0 + (R_S_INFO / max(r_kpc, 1e-6))**2
    return epsilon ** (-N_COHERENCE)


def gradiente_coerencia(r_kpc, R_d):
    """
    Modelo mínimo para o gradiente informacional:
    I(r)/I0 = 1 + k * (r / R_d)
    
    Esse termo substitui a necessidade de matéria escura.
    """
    return 1.0 + K_TGU * (r_kpc / R_d)


# ============================================================
# VELOCIDADES ORBITAIS
# ============================================================

def velocidade_newtoniana(r_kpc, M_r):
    """
    Velocidade circular newtoniana padrão.
    """
    r_m = r_kpc * KPC
    return np.sqrt(G * M_r * M_SUN / r_m) / KM_S


def velocidade_tgu(r_kpc, M_r, R_d):
    """
    Velocidade orbital segundo a TGU (Equação 15).
    """
    v_newt = velocidade_newtoniana(r_kpc, M_r)
    boost_info = np.sqrt(gradiente_coerencia(r_kpc, R_d))
    coh_factor = np.sqrt(fator_coerencia(r_kpc))
    
    return v_newt * boost_info * coh_factor


# ============================================================
# SIMULAÇÃO DE UMA GALÁXIA ESPIRAL
# ============================================================

# Parâmetros típicos (Via Láctea-like)
M_DISK = 5.0e10    # massas solares
R_DISK = 3.0       # kpc

r_vals = np.linspace(0.2, 30.0, 400)

M_r_vals = massa_disco_exponencial(r_vals, M_DISK, R_DISK)

v_newton = [velocidade_newtoniana(r, m) for r, m in zip(r_vals, M_r_vals)]
v_tgu = [velocidade_tgu(r, m, R_DISK) for r, m in zip(r_vals, M_r_vals)]

# Curva "observada" fictícia (perfil plano típico)
v_obs_mock = 220.0 * (1.0 - np.exp(-r_vals / 2.0))

# ============================================================
# PLOT
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(r_vals, v_newton, 'r--', label='Newton (matéria visível)')
plt.plot(r_vals, v_tgu, 'b-', linewidth=2, label='TGU (gradiente de coerência)')
plt.plot(r_vals, v_obs_mock, 'k:', linewidth=2, label='Observado (mock)')

plt.xlabel('Raio galáctico (kpc)')
plt.ylabel('Velocidade circular (km/s)')
plt.title('Curva de Rotação Galáctica — TGU vs Newton')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
