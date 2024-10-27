"""
Editor de Spyder

Este es un archivo temporal.
"""
# Importar librerias necesarias
import pandas as pd
import matplotlib.pyplot as plt

# cargamos el archivo excel
file_path = 'living.csv' 
data = pd.read_csv(file_path)

# Iniciamos el Analisis del dataset

# Numero de filas y columnas
num_filas = data.shape[0]
num_columnas = data.shape[1]

# Costo de vida promedio
costo_vida_promedio = data["Cost of living, 2017"].mean()

# Pais con el costo de vida mas alto y mas bajo
pais_costo_alto = data.loc[data["Cost of living, 2017"].idxmax()]
pais_costo_bajo = data.loc[data["Cost of living, 2017"].idxmin()]

# Costo de vida y ranking para Peru
peru_data = data[data["Countries"] == "Peru"]

# Imprimir resultados
print(f"Numero de filas: {num_filas}")
print(f"Numero de columnas: {num_columnas}")
print(f"Costo de vida promedio: {costo_vida_promedio:.2f}")
print(f"Pais con mayor costo de vida: {pais_costo_alto['Countries']} ({pais_costo_alto['Cost of living, 2017']})")
print(f"Pais con menor costo de vida: {pais_costo_bajo['Countries']} ({pais_costo_bajo['Cost of living, 2017']})")
print(f"Costo de vida en Peru: {peru_data['Cost of living, 2017'].values[0] if not peru_data.empty else 'No disponible'}")
print(f"Ranking de Peru: {peru_data['Global rank'].values[0] if not peru_data.empty else 'No disponible'}")

# Realizamos las visualizaciones

# Grafico de los 10 paises con mayor costo de vida
top_10_costo_alto = data.nlargest(10, 'Cost of living, 2017')
plt.figure(figsize=(10, 6))
plt.barh(top_10_costo_alto['Countries'], top_10_costo_alto['Cost of living, 2017'], color='skyblue')
plt.gca().invert_yaxis()
plt.title("Top 10 países con mayor costo de vida en 2017")
plt.xlabel("Costo de Vida")
plt.ylabel("Países")
plt.savefig('Top 10 países con mayor costo de vida en 2017.png', dpi=300, bbox_inches='tight')
plt.show()

# Grafico de los 10 paises con menor costo de vida
top_10_costo_bajo = data.nsmallest(10, 'Cost of living, 2017')
plt.figure(figsize=(10, 6))
plt.barh(top_10_costo_bajo['Countries'], top_10_costo_bajo['Cost of living, 2017'], color='lightgreen')
plt.gca().invert_yaxis()
plt.title("Top 10 paises con menor costo de vida en 2017")
plt.xlabel("Costo de Vida")
plt.ylabel("Países")
plt.savefig('Top 10 paises con menor costo de vida en 2017.png', dpi=300, bbox_inches='tight')
plt.show()

# Grafico del costo de vida en países de America

america_data = data[data['Continent'] == 'America']
plt.figure(figsize=(10, 6))
plt.barh(america_data['Countries'], america_data['Cost of living, 2017'], color='salmon')
plt.gca().invert_yaxis()
plt.title("Costo de vida en paises de America en 2017")
plt.xlabel("Costo de Vida")
plt.ylabel("Países")
plt.savefig('Costo de vida en paises de America en 2017.png', dpi=300, bbox_inches='tight')
plt.show()

# Calcular el costo de vida promedio por continente
costo_vida_por_continente = data.groupby('Continent')['Cost of living, 2017'].mean().reset_index()

# Crear el grafico
plt.figure(figsize=(10, 6))
plt.bar(costo_vida_por_continente['Continent'], costo_vida_por_continente['Cost of living, 2017'], color='coral')
plt.title("Costo de Vida Promedio por Continente en 2017")
plt.xlabel("Continente")
plt.ylabel("Costo de Vida Promedio")
plt.xticks(rotation=45)
# Etiquetas en los valores de las barras
for index, value in enumerate(costo_vida_por_continente['Cost of living, 2017']):
    plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')

plt.savefig('Costo de Vida Promedio por Continente en 2017.png', dpi=300, bbox_inches='tight')
plt.show()

