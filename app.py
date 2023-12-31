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

# Otro botón (puedes cambiar a casilla de verificación según tus necesidades)
button_2 = st.button('Otro Botón')
if button_2:
    st.write('Haz clic en el segundo botón')

# Puedes agregar más visualizaciones, botones, casillas de verificación, etc.

# Asegúrate de que haya contenido en general
if not (hist_button or checkbox or button_2):
    st.warning('No se ha seleccionado ninguna opción. Seleccione al menos una para visualizar.')

# Asegúrate de cerrar la aplicación de Streamlit
st.balloons()