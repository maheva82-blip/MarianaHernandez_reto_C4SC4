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
st.title("Desempeño de los colaboradores - Area de Marketing")
st.write("Conociendo el desempeño de los colaboradores del Área de Marketing de Socialize your knowledge")

#  2. Código para desplegar el logotipo de la empresa
image = Image.open('logo.jpg')
st.logo(image,size="large")

#  3. Código para incluir un control para seleccionar
#     el género del empleado
#      Debido a que podemos mostrar ambos o cualquiera de los dos generos se opta por un multiselect
employee_data = pd.read_csv("Employee_data.csv")

# colocar valores por default
default_gender = employee_data['gender'].unique()
default_marital_status = employee_data['marital_status'].unique()

selected_gender = st.sidebar.multiselect("Selecciona el genero", employee_data['gender'].unique(), default = default_gender)

#  4. Código para incluir un control para seleccionar el rango del
#     puntaje de desempeño del empleado
perform_min, perform_max = st.sidebar.slider("Selecciona el score de performance",
                                      min_value=int(employee_data['performance_score'].min()),
                                      max_value=int(employee_data['performance_score'].max()), 
                                      step=1, 
                                      value=[int(employee_data['performance_score'].min()),int(employee_data['performance_score'].max())])
subset_performance = employee_data[employee_data['performance_score'].between(perform_min, perform_max)]
st.sidebar.write(f"Numero de empleados con desempeño entre {perform_min} y {perform_max}: {subset_performance.shape[0]}")


#  5. Código para incluir un control para seleccionar
#     el estado civil del empleado
selected_marital_status = st.sidebar.multiselect("Selecciona el estatus marital", employee_data['marital_status'].unique(), default = default_marital_status)

employee_filtered = employee_data[
    (employee_data['gender'].isin(selected_gender)) & 
    (employee_data['performance_score'].between(perform_min, perform_max)) &
    (employee_data['marital_status'].isin(selected_marital_status))
]

if not employee_filtered.empty:
#  6. Código para visualizar la distribución de los
#     puntajes de desempeño de los empleados

    fig6 = px.histogram(employee_filtered, 
                    y='performance_score', 
                    title='Cantidad de Empleados por Rubro de Desempeño',
                    color='performance_score',
                    text_auto=True   )         

    fig6.update_xaxes(tickangle=45)

    st.plotly_chart(fig6)

#  7. Código para visualizar el promedio de las
#     horas trabajadas por el género del empleado

    fig7 = px.box(employee_filtered, 
            x='gender', 
            y='average_work_hours', 
            color='gender',
            points="all", 
            hover_data=['name_employee'], # Para que al pasar el mouse diga quién es ese punto
            title='Promedio de horas trabajadas vs Genero'
        )
    st.plotly_chart(fig7)

#  8. Código para visualizar la edad de los empleados
#     con respecto al salario del empleado

    fig8 = px.scatter(employee_filtered, 
                  x='age', 
                  y= 'salary',
                  color='gender',
                  hover_data=['name_employee'],
                  title='Edad vs Salario por Genero')

    st.plotly_chart(fig8)

#  9. Código para visualizar la relación del promedio
#  de horas trabajadas versus el puntaje de desempeño

    fig9 = px.bar(employee_filtered, 
                  x='performance_score', 
                  y='average_work_hours',
                  color='gender',
                  barmode='group',
                  title='Performance Score vs Horas trabajadas')

    st.plotly_chart(fig9)



#  10. Código para desplegar las conclusiones del
#      análisis en la aplicación web



else:
    st.warning("No hay datos que coincidan con los filtros seleccionados.")