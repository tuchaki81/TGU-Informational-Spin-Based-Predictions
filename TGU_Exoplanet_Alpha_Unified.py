"""
TGU Unified Alpha Calculator for Selected Exoplanets - MASTER TGU Version
Author: Henry Matuchaki (@MatuchakiSilva)
Refined Formula: total_correction = alpha * coherence_factor
where alpha = 1 + k * (e / a)
coherence_factor = epsilon ** (-n), epsilon = 1 + (rs / r)**2, r ≈ a
"""

import numpy as np

# MASTER TGU Constants
K = 0.0881                  # Universal Informational Coupling (Matuchaki Parameter)
N = 12                      # Coherence Exponent (Harmonic Structure)
RS_INFORMATIONAL = 0.02391625  # Solar Coherence Radius (AU)

exoplanets = [
    {"name": "WASP-12b", "a": 0.0229, "e": 0.0486},
    {"name": "HD 80606b", "a": 0.449, "e": 0.9336},
    {"name": "Kepler-78b", "a": 0.0089, "e": 0.05},
    {"name": "GJ 436b", "a": 0.0287, "e": 0.152},
    {"name": "55 Cancri e", "a": 0.0156, "e": 0.05},
    {"name": "HD 209458b", "a": 0.047, "e": 0.014},
    {"name": "Tau Boo b", "a": 0.049, "e": 0.023},
    {"name": "HAT-P-2b", "a": 0.0677, "e": 0.5171},
    {"name": "Kepler-10b", "a": 0.0168, "e": 0.05},
    {"name": "WASP-33b", "a": 0.0256, "e": 0.0}
]

print("Exoplaneta           |  a (UA)  |  e       |  e/a     |  alpha   | Coherence Factor | Total Correction")
print("---------------------|----------|----------|----------|----------|------------------|------------------")
for exo in exoplanets:
    a = exo["a"]
    e = exo["e"]
    e_a = e / a
    alpha = 1 + K * e_a
    
    # MASTER TGU Coherence Factor
    epsilon = 1.0 + (RS_INFORMATIONAL / a) ** 2
    coherence_factor = epsilon ** (-N)
    
    total_correction = alpha * coherence_factor
    
    print(f"{exo['name']:<20} | {a:<8.4f} | {e:<8.4f} | {e_a:<8.4f} | {alpha:.6f} | {coherence_factor:.6f}         | {total_correction:.6f}")
