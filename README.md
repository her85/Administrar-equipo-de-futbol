# Administrador de un equipo de fútbol

## Descripción
Proyecto para gestionar y analizar datos de un equipo de fútbol, permitiendo cargar información de partidos, visualizar estadísticas y generar reportes.

## Características
- Carga de datos desde archivo Excel
- Análisis básico de partidos (goles, victorias, derrotas, empates)
- Visualización de estadísticas en consola
- Estructura lista para ampliar con visualizaciones o interfaz gráfica

## Requisitos
- Python 3.x
- pandas

## Instalación
1. Clona el repositorio
2. Instala las dependencias:
   ```powershell
   pip install pandas
   ```
3. Ejecuta el dashboard:
   ```powershell
   python dashboard.py
   ```

## Ejemplo de uso

1. Instala las dependencias necesarias:
   ```powershell
   pip install pandas matplotlib seaborn
   ```

2. Ejecuta el script en la terminal:
   ```powershell
   python dashboard.py
   ```

3. Se abrirán ventanas con gráficos automáticos y se mostrarán estadísticas en la consola.

## Archivos principales
- `dashboard.py`: Script principal para cargar y analizar los datos
- `datos_partidos.xlsx`: Archivo de datos de partidos

## Dependencias
- Python 3.x
- pandas
- matplotlib
- seaborn

## Notas
- El archivo de datos debe llamarse `datos_partidos.xlsx` y estar en el mismo directorio que el script.
- Si quieres usar una interfaz web, puedes adaptar el script con Streamlit (ver sugerencias de mejora).

## Sugerencias de mejora
- Agregar visualizaciones gráficas (matplotlib, seaborn)
- Implementar interfaz web (Streamlit, Dash)
- Añadir gestión de jugadores y estadísticas individuales

---
Proyecto educativo. No usar datos reales sin consentimiento.
