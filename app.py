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

# Alpha brut (performance relative cumulée)
alpha_brut = portfolio_perf - benchmark_perf

# Rendements actifs hebdomadaires
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
tracking_error_ann = 
