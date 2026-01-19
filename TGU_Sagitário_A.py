import numpy as np

# --- CONSTANTES FÍSICAS ---
G = 6.67430e-11          # Constante Gravitacional (m^3 kg^-1 s^-2)
c = 299792458            # Velocidade da luz (m/s)
M_SUN = 1.98847e30       # Massa Solar (kg)
AU = 1.495978707e11      # Unidade Astronômica em metros
RAD_TO_ARCMIN = (180/np.pi) * 60  # Conversão de radianos para minutos de arco

# --- PARÂMETROS TGU (MATUCHAKI, 2025) ---
K_MATUCHAKI = 0.0881     # Parâmetro de eficiência de coerência
N_COHERENCE = 12         # Expoente de resistência harmônica
RS_INFO = 0.02391625     # Raio informacional (em AU)

def calcular_precessao_sgr_a(massa_msun, a_au, e):
    """
    Calcula a precessão orbital comparando Relatividade Geral (RG) e TGU.
    """
    # 1. Cálculo da Precessão de Schwarzschild (Relatividade Geral)
    # Delta_Phi = (6 * pi * G * M) / (c^2 * a * (1 - e^2))
    massa_kg = massa_msun * M_SUN
    a_metros = a_au * AU
    
    phi_gr_rad = (6 * np.pi * G * massa_kg) / (c**2 * a_metros * (1 - e**2))
    
    # 2. Aplicação do Framework MASTER TGU
    # Fator Alpha: Correção por assimetria/excentricidade
    alpha = 1.0 + K_MATUCHAKI * (e / a_au)
    
    # Fator de Resistência de Coerência (Atenuação em campos fortes/próximos)
    # epsilon = 1 + (rs/r)^2
    epsilon = 1.0 + (RS_INFO / a_au)**2
    fator_coerencia = epsilon**(-N_COHERENCE)
    
    # Resultado TGU
    phi_tgu_rad = phi_gr_rad * alpha * fator_coerencia
    
    return {
        "gr_arcmin": phi_gr_rad * RAD_TO_ARCMIN,
        "tgu_arcmin": phi_tgu_rad * RAD_TO_ARCMIN,
        "alpha": alpha,
        "fator_coerencia": fator_coerencia,
        "desvio_percentual": ((phi_tgu_rad / phi_gr_rad) - 1) * 100
    }

# --- DADOS DA ESTRELA S2 (Sagitário A*) ---
massa_buraco_negro = 4.1e6  # 4.1 milhões de massas solares
semieixo_maior_s2 = 1031.0   # ~1031 AU
excentricidade_s2 = 0.8839

# Execução do Cálculo
res = calcular_precessao_sgr_a(massa_buraco_negro, semieixo_maior_s2, excentricidade_s2)

# --- OUTPUT DOS RESULTADOS ---
print(f"Simulação Sgr A* (Estrela S2):")
print(f"Precessão RG:  {res['gr_arcmin']:.6f} arcmin/órbita")
print(f"Precessão TGU: {res['tgu_arcmin']:.6f} arcmin/órbita")
print(f"Fator Alpha:   {res['alpha']:.8f}")
print(f"Resistência:   {res['fator_coerencia']:.10f}")
print(f"Diferença:     {res['desvio_percentual']:.4f}%")