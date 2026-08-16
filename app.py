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
tracking_error_ann = tracking_error_week * np.sqrt(WEEKS_PER_YEAR)

# ==========================================================
# ALPHA ANNUALISE
# ==========================================================

# Durée observée exprimée en années
years = n_obs / WEEKS_PER_YEAR

alpha_annualise = (1 + alpha_brut) ** (1 / years) - 1

# ==========================================================
# INFORMATION RATIO CORRIGE
# ==========================================================

information_ratio = alpha_annualise / tracking_error_ann

# ==========================================================
# HIT RATIO
# ==========================================================

hit_ratio = (active_returns > 0).mean()

# ==========================================================
# SHARPE SIMPLIFIE
# (sans taux sans risque)
# ==========================================================

weekly_mean_port = portfolio_returns.mean()
weekly_mean_bench = benchmark_returns.mean()

annual_return_port = (1 + weekly_mean_port) ** WEEKS_PER_YEAR - 1
annual_return_bench = (1 + weekly_mean_bench) ** WEEKS_PER_YEAR - 1

sharpe_port = annual_return_port / vol_ann_port
sharpe_bench = annual_return_bench / vol_ann_bench

# ==========================================================
# RESULTATS
# ==========================================================

results = pd.DataFrame({
    "Indicateur": [
        "Nb observations",
        "Performance absolue Portefeuille",
        "Performance absolue Indice",
        "Performance relative (Alpha brut)",
        "Alpha annualisé",
        "Volatilité hebdo Portefeuille",
        "Volatilité hebdo Indice",
        "Volatilité annualisée Portefeuille",
        "Volatilité annualisée Indice",
        "Beta",
        "Correlation",
        "Tracking Error hebdo",
        "Tracking Error annualisé",
        "Ratio Information corrigé",
        "Hit Ratio"
    ],
    "Valeur": [
        n_obs,
        portfolio_perf,
        benchmark_perf,
        alpha_brut,
        alpha_annualise,
        vol_week_port,
        vol_week_bench,
        vol_ann_port,
        vol_ann_bench,
        beta,
        correlation,
        tracking_error_week,
        tracking_error_ann,
        information_ratio,
        hit_ratio
    ]
})

# Formatage
for idx in results.index:
    if results.loc[idx, "Indicateur"] not in [
        "Nb observations",
        "Beta",
        "Correlation",
        "Ratio Information corrigé"
    ]:
        results.loc[idx, "Valeur"] = f"{results.loc[idx, 'Valeur']:.2%}"

print(results.to_string(index=False))
