
# TGU Unified Alpha Calculator for Selected Exoplanets
# Author: Henry Matuchaki (based on TGU - Teoria Unificada do Spin Informacional)
# Formula: alpha = 1 + k * (e / a), where k ≈ 0.088

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

k = 0.088  # TGU universal constant of coherence

print("Exoplaneta           |  a (UA)  |  e       |  e/a     |  alpha (TGU)")
print("---------------------|----------|----------|----------|--------------")
for exo in exoplanets:
    a = exo["a"]
    e = exo["e"]
    alpha = 1 + k * (e / a)
    e_a = e / a
    print(f"{exo['name']:<20} | {a:<8.4f} | {e:<8.4f} | {e_a:<8.4f} | {alpha:.6f}")
