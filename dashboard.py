import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Dashboard de Administrador de un equipo de futbol")

# Cargar datos de partidos desde Excel
def cargar_datos(ruta):
    try:
        df = pd.read_excel(ruta)
        print(f"Datos cargados correctamente: {len(df)} partidos.")
        return df
    except Exception as e:
        print("Error al cargar los datos:", e)
        return None

def mostrar_estadisticas(df):
    if df is None:
        print("No hay datos para analizar.")
        return
    print("\nEstadísticas generales:")
    print("Total de partidos:", len(df))
    if 'Goles a favor' in df.columns:
        print("Goles a favor:", df['Goles a favor'].sum())
    if 'Goles en contra' in df.columns:
        print("Goles en contra:", df['Goles en contra'].sum())
    if 'Resultado' in df.columns:
        print("Victorias:", (df['Resultado'] == 'Victoria').sum())
        print("Empates:", (df['Resultado'] == 'Empate').sum())
        print("Derrotas:", (df['Resultado'] == 'Derrota').sum())
        # Visualización de resultados
        plt.figure(figsize=(6,4))
        sns.countplot(x='Resultado', data=df, order=['Victoria','Empate','Derrota'])
        plt.title('Distribución de Resultados')
        plt.xlabel('Resultado')
        plt.ylabel('Cantidad')
        plt.tight_layout()
        plt.show()
    if 'Goles a favor' in df.columns and 'Goles en contra' in df.columns:
        # Histograma de goles
        plt.figure(figsize=(8,4))
        plt.hist(df['Goles a favor'], bins=15, alpha=0.7, label='Goles a favor')
        plt.hist(df['Goles en contra'], bins=15, alpha=0.7, label='Goles en contra')
        plt.title('Histograma de Goles a Favor y en Contra')
        plt.xlabel('Goles')
        plt.ylabel('Cantidad de partidos')
        plt.legend()
        plt.tight_layout()
        plt.show()

def main():
    ruta = 'datos_partidos.xlsx'
    df = cargar_datos(ruta)
    mostrar_estadisticas(df)

if __name__ == "__main__":
    main()