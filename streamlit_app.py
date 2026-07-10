# ##############################################
#  Reto: Conociendo el desempeño de los colaboradores 
#        el Área de Marketing de Socialize your knowledge
#    Mariana Hernández
################################################

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from PIL import Image


#  1. Código para desplegar el títuloy descripción
st.title("Conociendo el desempeño de los colaboradores - Area de Marketing")

#  2. Código para desplegar el logotipo de la empresa
image = Image.open('logo.jpg')
st.logo(image,size="large")

#  3. Código para incluir un control para seleccionar
#     el género del empleado
employee_data = pd.read_csv("Employee_data.csv")
selected_gender = st.sidebar.radio("Select Gender", employee_data['gender'].unique())

#  4. Código para incluir un control para seleccionar el rango del
#     puntaje de desempeño del empleado
perform_min, perform_max = st.sidebar.slider("Select the performance score",
                                      min_value=int(employee_data['performance_score'].min()),
                                      max_value=int(employee_data['performance_score'].max()), 
                                      step=1, 
                                      value=[int(employee_data['performance_score'].min()),int(employee_data['performance_score'].max())])
subset_performance = employee_data[employee_data['performance_score'].between(perform_min, perform_max)]
st.write(f"Number of records with Performance between {perform_min} and {perform_max}: {subset_performance.shape[0]}")


#  5. Código para incluir un control para seleccionar
#     el estado civil del empleado
selected_marital_status = st.sidebar.multiselect("Select Marital Status", employee_data['marital_status'].unique())


#  6. Código para visualizar la distribución de los
#     puntajes de desempeño de los empleados

fig6 = px.histogram(employee_data, 
                    y='performance_score', 
                    title='Cantidad de Empleados por Rubro de Desempeño',
                    color='performance_score',
                    text_auto=True   )         

fig6.update_layout(xaxis=dict(tickmode='linear', tick0=1, dtick=1))

st.plotly_chart(fig6)

#  7. Código para visualizar el promedio de las
#     horas trabajadas por el género del empleado

fig7 = px.box(
    employee_data, 
    x='gender', 
    y='average_work_hours', 
    color='gender',
    points="all", 
    hover_data=['name_employee'], # Para que al pasar el mouse diga quién es ese punto
    title='Average Working Hours vs Gender'
)
st.plotly_chart(fig7)

#  8. Código para visualizar la edad de los empleados
#     con respecto al salario del empleado


#  9. Código para visualizar la relación del promedio
#  de horas trabajadas versus el puntaje de desempeño


#  10. Código para desplegar las conclusiones del
#      análisis en la aplicación web
