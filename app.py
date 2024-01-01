import pandas as pd 
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Encabezado con texto
st.header('Análisis de Datos de Vehículos en Estados Unidos')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión
st.subheader('Gráfico de Dispersión: Precio vs. Año')
fig_scatter = px.scatter(car_data, x='model_year', y='price')
st.plotly_chart(fig_scatter, use_container_width=True)

# Encabezado con texto
st.header('Gráfico de Dispersión Interactivo')

# Botón para cambiar el estilo del gráfico
button_change_style = st.button('Cambiar Estilo del Gráfico')

# Gráfico de dispersión inicial
fig_scatter = px.scatter(car_data, x='model_year', y='price', title='Gráfico de Dispersión')
st.plotly_chart(fig_scatter, use_container_width=True)

# Sección condicional basada en el botón
if button_change_style:
    # Cambiar el estilo del gráfico a línea si el botón se presiona
    fig_line = px.line(car_data, x='model_year', y='price', title='Gráfico de Línea')
    st.plotly_chart(fig_line, use_container_width=True)
    