import streamlit as st
import pandas as pd

# Título de la app
st.title("Análisis de Vehiculos")

# Cargar los datos


@st.cache_data
def cargar_datos():
    # Simulación de carga, reemplaza esto con tu CSV o fuente real
    df = pd.read_csv("vehicles_us.csv")  # Asegúrate de tener este archivo
    return df


df = cargar_datos()

# Mostrar tabla
st.subheader("Vista previa del dataset")
st.dataframe(df.head(50))  # Muestra los primeros 50 por rendimiento
