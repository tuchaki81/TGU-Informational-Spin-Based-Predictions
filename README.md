# 🌌 TGU Informational Spin-Based Predictions

This repository contains the Python source code implementing predictive simulations based on the **TGU – Unified Theory of Informational Spin**. The core formula used across all scripts is the empirical correction:

\[
\alpha = 1 + k \cdot \frac{e}{a}
\]

where:
- **α** is the correction factor to Newtonian and relativistic models,
- **e** is the orbital eccentricity,
- **a** is the semi-major axis (in AU),
- **k** is a dimensionless constant derived from multivariate regression (approximately `k ≈ 0.088`).

These predictions offer a **testable, informationally coherent alternative** to classical gravitational models, incorporating a novel interpretation of gravitational strain as an emergent property of spin coherence.

---

## 🔭 Included Planetary Models

| Script | Description |
|--------|-------------|
| `TGU_Prediction_Mercury_Unified.py` | Simulates Mercury’s orbit and α-corrected gravitational profile |
| `TGU_Prediction_Venus_Unified.py` | Venus orbit simulation with eccentricity-based α correction |
| `TGU_Prediction_Earth_Unified.py` | Earth's orbital structure using TGU’s α correction |
| `TGU_Prediction_Mars_Unified.py` | Predictive simulation for Mars within the TGU framework |
| `TGU_Prediction_Icarus.py` | Applies the TGU correction to the high-eccentricity asteroid 1566 Icarus |
| `TGU_Exoplanet_Alpha_Unified.py` | α-corrected predictions for 10 well-known exoplanets (e.g., TRAPPIST-1, Kepler-90, HD 10180) |

---

## ⚙️ Requirements

Make sure you have the following Python packages installed:

```bash
pip install numpy matplotlib
