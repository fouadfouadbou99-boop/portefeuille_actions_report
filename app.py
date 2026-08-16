import pandas as pd
import numpy as np

# ==========================================================
# DONNEES
# ==========================================================
# Remplacer ces deux séries par vos rendements hebdomadaires
# en décimal (ex: -0.35% = -0.0035)

portfolio_returns = pd.Series([
    # ...
])

benchmark_returns = pd.Series([
    # ...
])

# ==========================================================
# PARAMETRES
# ==========================================================

WEEKS_PER_YEAR = 52

# ==========================================================
# CALCULS DE BASE
# ==========================================================

n_obs = len(portfolio_returns)

# Performances cumulées
portfolio_perf = (1 + portfolio_returns).prod() - 1
benchmark_perf = (1 + benchmark_returns).prod() - 1

# Alpha brut
alpha_brut = portfolio_perf - benchmark_perf

# Rendements actifs
active_returns = portfolio_returns - benchmark_returns

# ==========================================================
# VOLATILITES
# ==========================================================

vol_week_port = portfolio_returns.std(ddof=1)
vol_week_bench = benchmark_returns.std(ddof=1)

vol_ann_port = vol_week_port * np.sqrt(WEEKS_PER_YEAR)
vol_ann_bench = vol_week_bench * np.sqrt(WEEKS_PER_YEAR)

# ==========================================================
# BETA ET CORRELATION
# ==========================================================

correlation = portfolio_returns.corr(benchmark_returns)

beta = (
    portfolio_returns.cov(benchmark_returns)
    / benchmark_returns.var(ddof=1)
)

# ==========================================================
# TRACKING ERROR
# ==========================================================

tracking_error_week = active_returns.std(ddof=1)
tracking_error_ann = tracking_error_week * np.sqrt(WEEKS_PER_YEAR)

# ==========================================================
# PERFORMANCE ACTIVE ANNUALISEE
# ==========================================================

active_return_mean_week = active_returns.mean()

active_return_annualise = (
    (1 + active_return_mean_week) ** WEEKS_PER_YEAR
) - 1

# ==========================================================
# INFORMATION RATIO CORRIGE
# ==========================================================

if tracking_error_ann > 0:
    information_ratio = (
        active_return_annualise / tracking_error_ann
    )
else:
    information_ratio = np.nan

# ==========================================================
# HIT RATIO
# ==========================================================

hit_ratio = (active_returns > 0).mean()

# ==========================================================
# SHARPE SIMPLIFIE
# ==========================================================

weekly_mean_port = portfolio_returns.mean()
weekly_mean_bench = benchmark_returns.mean()

annual_return_port = (
    (1 + weekly_mean_port) ** WEEKS_PER_YEAR
) - 1

annual_return_bench = (
    (1 + weekly_mean_bench) ** WEEKS_PER_YEAR
) - 1

sharpe_port = annual_return_port / vol_ann_port
sharpe_bench = annual_return_bench / vol_ann_bench

# ===============================
