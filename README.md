# 🐍 Python for Data Analysis

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

Exercises from my **Associate Degree in Data Science and Artificial Intelligence**, going from language fundamentals to cleaning and analyzing datasets with pandas.

*Code comments and console output are in Spanish.*

| # | Project | What it shows |
|---|---|---|
| 01 | [Fundamentals](01-fundamentos) | Data types, operators, conditionals and loops |
| 02 | [Inventory management system](02-sistema-gestion-inventario) | Console app with OOP, input validation and `filter` / `map` / `reduce` |
| 03 | [Shipping analysis with pandas](03-analisis-envios-pandas) | Synthetic data generation, quality checks, integration, aggregations and outliers |

---

## 03 · Shipping analysis with pandas ⭐

A logistics case with data **generated on purpose with errors**, to practice data quality checks before the analysis.

**`generador_datos.py`** creates 3 datasets with `random.seed(25)` so they are reproducible:
- `envios_practica.csv` (80 shipments) with planted errors: missing distribution center, negative weight, zero cost, exaggerated delivery time, misspelled status, out-of-range date and a duplicate record.
- `envios_extra.csv` (40 more shipments).
- `info_ciudades.csv` (province, region, population, distance).

**`analisis.py`** runs the full workflow:
1. **Exploration:** shape, data types and missing values.
2. **Quality checks:** negative weights, zero costs, invalid statuses, duplicates and out-of-range dates.
3. **Integration:** `concat` of both datasets and `merge` with the city information.
4. **Aggregations:** cost per city, average time per center, packages per type and weight per province.
5. **Outliers:** delivery times above Q3 + 1.5·IQR.

```bash
cd 03-analisis-envios-pandas
python generador_datos.py
python analisis.py
```

## 02 · Inventory management system

Console app for a repair service: lists the catalog as a table (`tabulate`), registers orders with stock and input validation, stores customers as objects (`class Cliente`) and analyzes the inventory with functional programming (`filter` by material, `map` to simulate discounts, `reduce` for the total value) and a `set` for unique locations.

```bash
cd 02-sistema-gestion-inventario
python main.py
```

## ⚙️ Requirements

```bash
pip install -r requirements.txt
```
