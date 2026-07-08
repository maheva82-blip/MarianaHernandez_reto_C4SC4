# ##############################################
#  Reto: Conociendo el desempeño de los colaboradores 
#        el Área de Marketing de Socialize your knowledge
#    Mariana Hernández
################################################

import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image


#  1. Código para desplegar el títuloy descripción
st.title("Conociendo el desempeño de los colaboradores - Area de Marketing")

#  2. Código para desplegar el logotipo de la empresa
image = Image.open('logo.jpg')
st.image(image,caption='')

#  3. Código para incluir un control para seleccionar
#     el género del empleado
employee_data = pd.read_csv("Employee_data.csv")
selected_gender = st.radio("Select Gender", employee_data['gender'].unique())

#  4. Código para incluir un control para seleccionar el rango del
#     puntaje de desempeño del empleado
optionals = st.beta_expander("Optional configurations",True)
performance_select = optionals.slider("Select the performance score",
                                      min_value=int(employee_data['performance_score']),
                                      max_value=int(employee_data['performance_score']))
subset_performance = employee_data[(employee_data['performance_score']>=performance_select)]
st.write(f"Number of records with this Performance {performance_select}: {subset_performance.shape[0]}")


#  5. Código para incluir un control para seleccionar
#     el estado civil del empleado
selected_marital_status = st.radio("Select Marital Status", employee_data['marital_status'].unique())


#  6. Código para visualizar la distribución de los
#     puntajes de desempeño de los empleados


#  7. Código para visualizar el promedio de las
#     horas trabajadas por el género del empleado
fig = px.line(df, x="average_work_hours", y="gender", title='Average Working Hours vs Gender’)
st.plotly_chart(fig, use_container_width=True)

#  8. Código para visualizar la edad de los empleados
#     con respecto al salario del empleado


#  9. Código para visualizar la relación del promedio
#  de horas trabajadas versus el puntaje de desempeño


#  10. Código para desplegar las conclusiones del
#      análisis en la aplicación web
