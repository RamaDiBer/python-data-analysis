import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(25)

# -----------------------------
# Datos auxiliares
# -----------------------------

ciudades = [
    ("La Rioja", "La Rioja", "NOA"),
    ("Córdoba", "Córdoba", "Centro"),
    ("Rosario", "Santa Fe", "Centro"),
    ("Mendoza", "Mendoza", "Cuyo"),
    ("Salta", "Salta", "NOA"),
    ("Neuquén", "Neuquén", "Patagonia"),
    ("Posadas", "Misiones", "NEA"),
    ("Resistencia", "Chaco", "NEA")
]

centros = [
    "Centro Norte",
    "Centro Sur",
    "Centro Oeste"
]

tipos = [
    "Express",
    "Normal",
    "Económico"
]

estados = [
    "Entregado",
    "Retrasado",
    "Cancelado"
]

# -----------------------------
# Función para generar envíos
# -----------------------------

def generar_envios(cantidad, fecha_inicio):

    registros = []

    for i in range(cantidad):

        ciudad = random.choice(ciudades)

        fecha = fecha_inicio + timedelta(days=random.randint(0,25))

        registro = {
            "Fecha": fecha.strftime("%Y-%m-%d"),
            "Guia": 1000+i,
            "Centro": random.choice(centros),
            "Ciudad": ciudad[0],
            "Tipo_Envio": random.choice(tipos),
            "Peso_kg": round(random.uniform(0.5,20),2),
            "Tiempo_Entrega_hs": random.randint(12,120),
            "Costo": random.randint(3000,30000),
            "Estado": random.choice(estados)
        }

        registros.append(registro)

    return pd.DataFrame(registros)

# -----------------------------
# Base principal
# -----------------------------

df = generar_envios(
    cantidad=80,
    fecha_inicio=datetime(2025,5,1)
)

# -----------------------------
# Introducir errores intencionales
# -----------------------------

# Centro faltante
df.loc[5,"Centro"] = None

# Peso negativo
df.loc[11,"Peso_kg"] = -4

# Costo cero
df.loc[18,"Costo"] = 0

# Tiempo exagerado
df.loc[27,"Tiempo_Entrega_hs"] = 450

# Estado incorrecto
df.loc[36,"Estado"] = "Entrgado"

# Fecha fuera de rango
df.loc[45,"Fecha"] = "2028-01-15"

# Registro duplicado
df.loc[70] = df.loc[10]

df.to_csv("envios_practica.csv",index=False)

# -----------------------------
# Base adicional
# -----------------------------

df2 = generar_envios(
    cantidad=40,
    fecha_inicio=datetime(2025,6,1)
)

df2.to_csv("envios_extra.csv",index=False)

# -----------------------------
# Información de ciudades
# -----------------------------

info = []

for ciudad,provincia,region in ciudades:

    info.append({

        "Ciudad": ciudad,
        "Provincia": provincia,
        "Region": region,
        "Habitantes": random.randint(80000,1500000),
        "Distancia_km": random.randint(80,1800),
        "Altitud_m": random.randint(5,1500),
        "Temperatura_Promedio": round(random.uniform(10,25),1),
        "Indice_Economico": round(random.uniform(0.5,1.5),2)

    })

df_info = pd.DataFrame(info)

df_info.to_csv("info_ciudades.csv",index=False)

print("Archivos generados correctamente.")