import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado de la app
st.header("Análisis de Vehículos Usados en EE.UU.")

# Cargar datos


@st.cache_data
def cargar_datos():
    df = pd.read_csv("vehicles_us.csv")
    return df


df = cargar_datos()

# Vista previa del dataset
st.subheader("Vista previa del conjunto de datos")
st.dataframe(df.head(50))

# Botón para histograma
st.subheader("Distribución del precio de los vehículos")
if st.button("Mostrar histograma de precios"):
    fig_hist = px.histogram(df, x="price", nbins=50,
                            title="Histograma de Precios")
    st.plotly_chart(fig_hist)

# Botón para gráfico de dispersión
st.subheader("Relación entre año y precio del vehículo")
if st.button("Mostrar gráfico de dispersión"):
    fig_scatter = px.scatter(
        df,
        x="model_year",
        y="price",
        color="transmission",
        title="Gráfico de Dispersión: Año del modelo vs. Precio",
        labels={"model_year": "Año del modelo", "price": "Precio"}
    )
    st.plotly_chart(fig_scatter)
