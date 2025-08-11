# Yield Curve Modeling: Nelson–Siegel vs. Cubic Spline

## Overview
This project analyzes Indian Government Securities (G-Secs) yields across multiple maturities and compares two yield curve fitting approaches:
1. **Nelson–Siegel Model**
2. **Cubic Spline Interpolation**

The aim is to:
- Model the yield curve using short-to-long maturities (6 months to 30 years).
- Compare the fits in terms of accuracy and interpretability.
- Discuss the ethics of smoothing yield curve data.

---

## Data
- **Source**: `yields.csv` containing daily G-Sec yields.
- **Maturities**: 3M, 6M, 1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 13Y, 15Y, 24Y, 30Y.
- **Cleaning**:  
  - Removed rows where **any maturity yield > 11%** (to eliminate outliers).
  - No missing values after cleaning.

---

## Exploratory Analysis

### Treasury Yields Over Time
![Treasury Yields](images/TreasuryYeilds.png )

### Pairwise Distribution and KDE
![Pairwise KDE](images/pairwise_kde.png)

### Example Yield Curve (2020-01-03)
![Yield Curve 2020-01-03](images/yield_curve_2020-01-03.png)

---

## Model Fitting

### Nelson–Siegel Model
Parametric model:
\[
y(t) = \beta_0 + (\beta_1 + \beta_2) \frac{1 - e^{-t/\tau}}{t/\tau} - \beta_2 e^{-t/\tau}
\]

- **β₀**: Long-term rate level  
- **β₁**: Short-term slope  
- **β₂**: Medium-term curvature  
- **τ**: Decay factor controlling hump position  

Fitted using:
```python
from nelson_siegel_svensson.calibrate import calibrate_ns_ols
curve_ns, status = calibrate_ns_ols(t, y, tau0=1.0)
