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

# Casilla de verificación
checkbox = st.checkbox('Mostrar Detalles Adicionales')
if checkbox:
    # Contenido adicional cuando la casilla está marcada
    st.write('Detalles adicionales...')

filter_button = st.button('Filtrar Datos')
if filter_button:
    # Lógica de filtrado
    min_year = st.slider('Año Mínimo', int(car_data['model_year'].min()), int(car_data['model_year'].max()), int(car_data['model_year'].min()))
    max_year = st.slider('Año Máximo', min_year, int(car_data['model_year'].max()), int(car_data['model_year'].max()))

    min_price = st.slider('Precio Mínimo', int(car_data['price'].min()), int(car_data['price'].max()), int(car_data['price'].min()))
    max_price = st.slider('Precio Máximo', min_price, int(car_data['price'].max()), int(car_data['price'].max()))

    filtered_data = car_data[(car_data['model_year'] >= min_year) & (car_data['model_year'] <= max_year) & (car_data['price'] >= min_price) & (car_data['price'] <= max_price)]

    # Mostrar datos filtrados
    st.subheader('Datos Filtrados')
    st.write(filtered_data)
    