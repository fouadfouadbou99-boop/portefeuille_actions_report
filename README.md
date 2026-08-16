# Reporting Comité Actions RPC

Application Streamlit permettant de générer automatiquement un reporting de portefeuille Actions RPC à partir d'un fichier Excel.

## Fonctionnalités

- Chargement d'un fichier Excel
- Calcul automatique des KPI
- Synthèse exécutive
- Analyse de la performance
- Analyse du risque
- Analyse de la gestion active
- Recommandations automatiques
- Note au Comité
- Export Excel
- Export PDF

## Structure du fichier Excel

Le classeur doit contenir :

### Feuille 1 : Données historiques

| Date | Portefeuille | ... | Benchmark |
|--------|--------|--------|--------|

### Feuille 2 : KPI

| Indicateur | Valeur |
|------------|---------|
| Performance absolue Portefeuille | ... |
| Performance absolue Indice | ... |
| Performance relative (Alpha brut) | ... |
| Beta | ... |
| Correlation | ... |
| Tracking Error annualise | ... |
| Ratio Information | ... |
| Hit Ratio | ... |
| Volatilite annualisee Portefeuille | ... |
| Volatilite annualisee Indice | ... |

### Feuille 3 : Active Returns

Distribution des rendements actifs.

## Installation

Créer un environnement virtuel :

```bash
python -m venv venv
