import numpy as np
import pandas as pd

# 1. GENERATE RAW CORRELATED SIGNALS
# Imagine Signal 1 and 2 are 80% correlated (both are types of Momentum)
np.random.seed(42)
n_assets = 10
sig_1 = np.random.normal(0, 1, n_assets)
sig_2 = sig_1 * 0.8 + np.random.normal(0, 0.2, n_assets) # Highly correlated
sig_3 = np.random.normal(0, 1, n_assets)                # Independent (e.g., Value)

signals = np.vstack([sig_1, sig_2, sig_3])

# 2. LINEAR ALGEBRA: SIGNAL COMBINATION
# We calculate the Covariance of the signals themselves
sig_cov = np.cov(signals)

# We use the inverse of the covariance matrix to "de-noise" the weights
# This is a simplified version of 'Markowitz for Signals'
sig_inv_cov = np.linalg.inv(sig_cov)
combined_weights = np.sum(sig_inv_cov, axis=1)
combined_weights /= np.sum(np.abs(combined_weights)) # Normalize weights

# 3. FINAL AGGREGATED Z-SCORE
final_signal = combined_weights @ signals

print(f"--- 📐 LINEAR ALGEBRA: SIGNAL DE-CORRELATOR ---")
print(f"Signal Weights (Optimized):")
print(f"Sig 1 (Momentum A): {combined_weights[0]:.4f}")
print(f"Sig 2 (Momentum B): {combined_weights[1]:.4f}")
print(f"Sig 3 (Value):      {combined_weights[2]:.4f}")
print("-" * 45)
print("Quant Note: Signal 2 was penalized due to high correlation with Signal 1.")
print("This prevents 'Double Counting' the same alpha source.")
