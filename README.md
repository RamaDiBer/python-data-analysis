# 🐍 Python para análisis de datos

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

Prácticas de la **Tecnicatura en Ciencia de Datos e Inteligencia Artificial**. Van desde los fundamentos del lenguaje hasta la limpieza y el análisis de datasets con pandas.

| # | Proyecto | Qué muestra |
|---|---|---|
| 01 | [Fundamentos](01-fundamentos) | Tipos de datos, operadores, condicionales y bucles |
| 02 | [Sistema de gestión de inventario](02-sistema-gestion-inventario) | App de consola con POO, validación de entradas y `filter` / `map` / `reduce` |
| 03 | [Análisis de envíos con pandas](03-analisis-envios-pandas) | Generación de datos sintéticos, control de calidad, integración, agregaciones y outliers |

---

## 03 · Análisis de envíos con pandas ⭐

Un caso de logística con datos **generados a propósito con errores**, para practicar el control de calidad antes del análisis.

**`generador_datos.py`** crea 3 datasets con `random.seed(25)`, así se pueden reproducir:
- `envios_practica.csv` (80 envíos) con errores plantados: centro faltante, peso negativo, costo cero, tiempo de entrega exagerado, estado mal escrito, fecha fuera de rango y un registro duplicado.
- `envios_extra.csv` (40 envíos más).
- `info_ciudades.csv` (provincia, región, habitantes, distancia).

**`analisis.py`** hace el recorrido completo:
1. **Exploración**: dimensiones, tipos y valores faltantes.
2. **Control de calidad**: pesos negativos, costos cero, estados inválidos, duplicados y fechas fuera de rango.
3. **Integración**: `concat` de las dos bases y `merge` con la información de ciudades.
4. **Agregaciones**: costo por ciudad, tiempo promedio por centro, paquetes por tipo y peso por provincia.
5. **Outliers**: tiempos de entrega por encima de Q3 + 1,5·IQR.

```bash
cd 03-analisis-envios-pandas
python generador_datos.py
python analisis.py
```

## 02 · Sistema de gestión de inventario

App de consola para un servicio técnico: lista el catálogo en tabla (`tabulate`), registra pedidos con validación de stock y de entradas, guarda clientes como objetos (`class Cliente`) y analiza el inventario con programación funcional (`filter` por material, `map` para simular descuentos, `reduce` para el valor total) y `set` para localidades únicas.

```bash
cd 02-sistema-gestion-inventario
python main.py
```

## ⚙️ Requisitos

```bash
pip install -r requirements.txt
```
