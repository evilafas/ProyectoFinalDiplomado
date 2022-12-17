
from pandas import json_normalize
import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import json
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")

st.header("DASHBOARD")
st.sidebar.header("REGISTRO DE LOS PROCESOS DE COMPRA, SEAN ADJUDICADO O NO ADJUDICADOS, HECHOS EN LA PLATAFORMA SECOP DESDE SU LANZAMIENTO")
st.sidebar.markdown("---")
st.markdown("# APARTADO DE GRAFICAS Y TABLAS")

servidor = 'http://18.205.133.251:8000/'

@st.cache
def cargar_datos():
    response = requests.get(servidor + '/datos')
    info = json.loads(response.text)    
    datos = json_normalize(info)
    return datos

def get_entidades_departamento():
    response = requests.get(servidor + '/entidades_departamento')
    info = json.loads(response.text)    
    datos = json_normalize(info)
    return datos

def get_entidades_ciudad():
    response = requests.get(servidor + '/entidades_ciudad')
    info = json.loads(response.text)    
    datos = json_normalize(info)
    return datos

def get_media_precio_base():
    response = requests.get(servidor + '/media_precio_base')
    info = json.loads(response.text)    
    datos = json_normalize(info)
    return datos
    
def get_modalidad_contratos():
    response = requests.get(servidor + '/modalidad_contratos')
    info = json.loads(response.text)    
    datos = json_normalize(info)
    return datos

def get_tipo_contratos():
    response = requests.get(servidor + '/tipo_contratos')
    info = json.loads(response.text)    
    datos = json_normalize(info)
    return datos

def get_estado():
    response = requests.get(servidor + '/estado')
    info = json.loads(response.text)    
    datos = json_normalize(info)
    return datos

def get_costos_año():
    response = requests.get(servidor + '/costos_año')
    info = json.loads(response.text)    
    datos = json_normalize(info)
    return datos

def get_estado_procedimiento():
    response = requests.get(servidor + '/estado_procedimiento')
    info = json.loads(response.text)    
    datos = json_normalize(info)
    return datos

def get_procesos_departamentos():
    response = requests.get(servidor + '/procesos_departamentos')
    info = json.loads(response.text)    
    datos = json_normalize(info)
    return datos

def get_prediccion():
    response = requests.get(servidor + '/prediccion')
    info = json.loads(response.text)    
    # datos = json_normalize(info)
    datos = (info)
    return datos



datos = cargar_datos()
radio_button = st.sidebar.radio(
    label="Tabla de datos", options=["Mostrar", "No mostrar"]
)

opciones_select = ['Tablas y graficas', 'Tablas', 'Graficas']
modo_vista = st.sidebar.selectbox(
    label="Seleccione un modo de vista", options=opciones_select
)

if radio_button == "Mostrar":
    st.dataframe(datos)

entidades_departamento = get_entidades_departamento()
entidades_departamento = entidades_departamento.transpose()
entidades_departamento = entidades_departamento.reset_index()
entidades_departamento.rename(columns = {'index':'departamento',  0:'cantidad'}, inplace = True) 
# st.write(entidades_departamento)

entidades_ciudad = get_entidades_ciudad()
entidades_ciudad = entidades_ciudad.transpose()
entidades_ciudad = entidades_ciudad.reset_index()
entidades_ciudad.rename(columns = {'index':'ciudad',  0:'cantidad'}, inplace = True) 
# st.write(entidades_ciudad)

media_precio_base = get_media_precio_base()
media_precio_base = media_precio_base.transpose()
media_precio_base = media_precio_base.reset_index()
media_precio_base.rename(columns = {'index':'departamento',  0:'media de precio'}, inplace = True) 
media_precio_base['media de precio'] = media_precio_base['media de precio'].astype(float)
media_precio_base.round({"media de precio":2}) 
# st.write(media_precio_base)

colum1,colum2, colum3  = st.columns(3)

colum1.subheader("Cantidad de entidades por departamentos") 
colum1.write(entidades_departamento)
colum2.subheader("Cantidad de entidades por ciudad") 
colum2.write(entidades_ciudad)
colum3.subheader("Media de los precios bases agrupados por departamento") 
colum3.write(media_precio_base)

st.subheader("Modalidades de contratos") 
modalidad_contratos = get_modalidad_contratos()
modalidad_contratos = modalidad_contratos.transpose()
modalidad_contratos = modalidad_contratos.reset_index()
modalidad_contratos.rename(columns = {'index':'modalidad',  0:'cantidad'}, inplace = True) 
fig_modalidad_contratos = px.bar(modalidad_contratos, x="modalidad", y="cantidad", text_auto='.2s', color='cantidad')
fig_modalidad_contratos.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

if modo_vista == opciones_select[0]:
    st.write(modalidad_contratos)
    st.plotly_chart(fig_modalidad_contratos, use_container_width=True)
elif modo_vista == opciones_select[1]:
    st.write(modalidad_contratos)
elif modo_vista == opciones_select[2]:
    st.plotly_chart(fig_modalidad_contratos, use_container_width=True)



st.subheader("Tipos de contratos") 
tipo_contratos = get_tipo_contratos()
tipo_contratos = tipo_contratos.transpose()
tipo_contratos = tipo_contratos.reset_index()
tipo_contratos.rename(columns = {'index':'tipo_contrato',  0:'cantidad'}, inplace = True) 
fig_tipo_contratos = px.bar(tipo_contratos, x="cantidad", y="tipo_contrato", text_auto='.2s', orientation="h", color='tipo_contrato')
fig_tipo_contratos.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

if modo_vista == opciones_select[0]:
    st.write(tipo_contratos)
    st.plotly_chart(fig_tipo_contratos, use_container_width=True)
elif modo_vista == opciones_select[1]:
    st.write(tipo_contratos)
elif modo_vista == opciones_select[2]:
    st.plotly_chart(fig_tipo_contratos, use_container_width=True)


st.subheader("Estados de los contratos") 
estado = get_estado()
estado = estado.transpose()
estado = estado.reset_index()
estado.rename(columns = {'index':'estado',  0:'cantidad'}, inplace = True) 
fig_estado = px.pie(estado, values="cantidad", names="estado",color='estado', color_discrete_map={'Cerrado':'lightcyan','Abierto':'darkblue'}) 

if modo_vista == opciones_select[0]:
    st.write(estado)
    st.plotly_chart(fig_estado, use_container_width=True)

elif modo_vista == opciones_select[1]:
    st.write(estado)
elif modo_vista == opciones_select[2]:
    st.plotly_chart(fig_estado, use_container_width=True)

st.subheader("Procesos por año") 
costos_año = get_costos_año()
costos_año = costos_año.transpose()
costos_año = costos_año.reset_index()
costos_año.rename(columns = {'index':'año',  0:'cantidad'}, inplace = True) 
fig_costos_año = px.line(x=costos_año['año'], y=costos_año['cantidad'], labels={'x':'ANIOS', 'y':'CANTIDAD'}, markers=True)


if modo_vista == opciones_select[0]:
    st.write(costos_año)
    st.plotly_chart(fig_costos_año, use_container_width=True)
elif modo_vista == opciones_select[1]:
    st.write(costos_año)
elif modo_vista == opciones_select[2]:
    st.plotly_chart(fig_costos_año, use_container_width=True)

st.subheader("Estados de los procedimientos") 
estado_procedimiento = get_estado_procedimiento()
estado_procedimiento = estado_procedimiento.transpose()
estado_procedimiento = estado_procedimiento.reset_index()
estado_procedimiento.rename(columns = {'index':'estado',  0:'cantidad'}, inplace = True) 
fig_estado_procedimiento = px.pie(estado_procedimiento, values="cantidad", names="estado", color_discrete_sequence=px.colors.sequential.RdBu) 

if modo_vista == opciones_select[0]:
    st.write(estado_procedimiento)
    st.plotly_chart(fig_estado_procedimiento, use_container_width=True)  
elif modo_vista == opciones_select[1]:
    st.write(estado_procedimiento)
elif modo_vista == opciones_select[2]:
    st.plotly_chart(fig_estado_procedimiento, use_container_width=True)

st.subheader("Departamentos con el numero de procedimientos") 
procesos_departamentos = get_procesos_departamentos()
procesos_departamentos = procesos_departamentos.transpose()
procesos_departamentos = procesos_departamentos.reset_index()
procesos_departamentos.rename(columns = {'index':'departamento',  0:'cantidad'}, inplace = True) 
fig_procesos_departamentos = px.bar(procesos_departamentos, x="departamento", y="cantidad", text_auto='.2s', color='departamento')
fig_procesos_departamentos.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)


if modo_vista == opciones_select[0]:
    st.write(procesos_departamentos)
    st.plotly_chart(fig_procesos_departamentos, use_container_width=True)
elif modo_vista == opciones_select[1]:
    st.write(procesos_departamentos)
elif modo_vista == opciones_select[2]:
    st.plotly_chart(fig_procesos_departamentos, use_container_width=True)


st.subheader("Prediccion para el año 2023")
predic = get_prediccion()
st.write("Varianza de la predicción: " + str(predic[0]))
st.write("Prediccion para cantidad de procesos: " + str(predic[1]))
