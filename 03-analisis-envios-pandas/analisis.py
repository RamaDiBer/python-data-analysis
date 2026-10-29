"""
Práctica Integradora 2
Alumno: Ramiro Di Bernardo

Análisis de datos con Pandas:
- Importación de datos
- Integración de datasets
- Agregaciones
- Control de calidad
- Detección de valores atípicos
"""
import pandas as pd

envios = pd.read_csv("envios_practica.csv")
extra = pd.read_csv("envios_extra.csv")
ciudades = pd.read_csv("info_ciudades.csv")

print("Dimensiones:")
print(envios.shape)

print("\nPrimeras filas:")
print(envios.head())

print("\nTipos de datos:")
print(envios.dtypes)

print("\nValores faltantes:")
print(envios.isnull().sum())

print("\nPESOS NEGATIVOS")
print(envios[envios["Peso_kg"] < 0])


print("\nCOSTOS CERO")
print(envios[envios["Costo"] == 0])

estados_validos = ["Entregado", "Retrasado", "Cancelado"]

print("\nESTADOS INCORRECTOS")
print(
    envios[
        ~envios["Estado"].isin(estados_validos)
    ]
)

print("\nDUPLICADOS")
print(envios[envios.duplicated()])

envios_total = pd.concat(
    [envios, extra],
    ignore_index=True
)

print("\nCantidad total de registros:")
print(envios_total.shape)

envios_total = envios_total.merge(
    ciudades,
    on="Ciudad",
    how="left"
)

print(envios_total.head())

print("\nCOSTO TOTAL POR CIUDAD")
costo_ciudad = envios_total.groupby("Ciudad")["Costo"].sum()
print(costo_ciudad)

print("\nTIEMPO PROMEDIO POR CENTRO")
tiempo_centro = envios_total.groupby("Centro")["Tiempo_Entrega_hs"].mean()
print(tiempo_centro)

print("\nCANTIDAD DE PAQUETES POR TIPO DE ENVIO")
cantidad_tipo = envios_total.groupby("Tipo_Envio").size()
print(cantidad_tipo)

print("\nPESO PROMEDIO POR PROVINCIA")
peso_provincia = envios_total.groupby("Provincia")["Peso_kg"].mean()
print(peso_provincia)

envios_total["Fecha"] = pd.to_datetime(envios_total["Fecha"])

fechas_invalidas = envios_total[
    envios_total["Fecha"] > "2025-12-31"
]

print("\nFECHAS FUERA DE RANGO")
print(fechas_invalidas)

print("\nREGISTROS CON DATOS FALTANTES")
print(envios_total[envios_total.isnull().any(axis=1)])

Q1 = envios_total["Tiempo_Entrega_hs"].quantile(0.25)
Q3 = envios_total["Tiempo_Entrega_hs"].quantile(0.75)

IQR = Q3 - Q1

limite_superior = Q3 + 1.5 * IQR

outliers = envios_total[
    envios_total["Tiempo_Entrega_hs"] > limite_superior
]

print("\nOUTLIERS TIEMPO ENTREGA")
print(outliers)

print(costo_ciudad.idxmax())
print(tiempo_centro.idxmin())
print(cantidad_tipo.idxmax())

