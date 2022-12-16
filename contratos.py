import pandas as pd
import numpy as np
import dask.dataframe as dd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score


class contratos:

    def __init__(self):
        # self.data = dd.read_csv("database/dataset.csv",
        #                         dtype={
        #                             'Fecha de Publicacion (Fase Borrador)': 'object',
        #                             'Fecha de Publicacion (Fase Seleccion Precalificacion)': 'object',
        #                             'Fecha de Publicacion (Manifestacion de Interes)': 'object',
        #                             'Fecha de Publicacion (Fase Planeacion Precalificacion)': 'object',
        #                         }, )
        # self.df = self.data.compute()
        self.df = pd.read_csv("database/dataset.csv", nrows=1000, dtype={
            'Fecha de Publicacion (Fase Borrador)': 'object',
            'Fecha de Publicacion (Fase Seleccion Precalificacion)': 'object',
            'Fecha de Publicacion (Manifestacion de Interes)': 'object',
            'Fecha de Publicacion (Fase Planeacion Precalificacion)': 'object',
        }, keep_default_na=False)

    def mostrarDatos(self):
        return self.df.to_dict(orient="records")

    def entidades_departamento(self):
        entidades_departamento = self.df.groupby("Departamento Entidad").agg({'Entidad': pd.Series.nunique})        
        return entidades_departamento.to_dict()['Entidad']

    def entidades_ciudad(self):
        entidades_ciudad = self.df.groupby("Ciudad Entidad").agg({'Entidad': pd.Series.nunique})
        return entidades_ciudad.to_dict()['Entidad']

    def media_precio_base(self):
        media_precio_base_departamento = self.df.groupby("Departamento Entidad").aggregate({'Precio Base': np.mean})
        return media_precio_base_departamento.to_dict()['Precio Base']

    def modalidad_contratos(self):
        modalidad_contratos = self.df["Modalidad de Contratacion"].value_counts().to_frame()
        return modalidad_contratos.to_dict()
        
    def tipos_contratos(self):        
        tipos_contratos = self.df["Tipo de Contrato"].value_counts().to_frame()
        return tipos_contratos.to_dict()["Tipo de Contrato"]

    def estado(self):        
        estado = self.df["Estado de Apertura del Proceso"].value_counts().to_frame()
        return estado.to_dict()["Estado de Apertura del Proceso"]

    def costos_año(self):
        self.df["Fecha de Publicacion del Proceso"] = pd.to_datetime(self.df["Fecha de Publicacion del Proceso"])
        self.df["año_Fecha_Publicacion_Proceso"] = self.df["Fecha de Publicacion del Proceso"].map(lambda x: x.year)   
        r = self.df["año_Fecha_Publicacion_Proceso"].value_counts().to_frame()     
        r = r.sort_index()
        t = r.index.tolist()
        s = r["año_Fecha_Publicacion_Proceso"].tolist()
        salida = pd.DataFrame(s, index = t, columns =['año']) 
        return salida.to_dict()['año']

    def estado_procedimiento(self):
        estado_procedimiento = self.df["Estado del Procedimiento"].value_counts().to_frame()
        return estado_procedimiento.to_dict()["Estado del Procedimiento"]

    def procesos_departamentos(self):
        departamentos = self.df["Departamento Entidad"].value_counts().to_frame()
        return departamentos.to_dict()['Departamento Entidad']

    def prediccionAnios(self):
        self.df["Fecha de Publicacion del Proceso"] = pd.to_datetime(self.df["Fecha de Publicacion del Proceso"])
        self.df["año_Fecha_Publicacion_Proceso"] = self.df["Fecha de Publicacion del Proceso"].map(lambda x: x.year)   
        r = self.df["año_Fecha_Publicacion_Proceso"].value_counts().to_frame()     
        r = r.sort_index()
        t = r.index.tolist()
        s = r["año_Fecha_Publicacion_Proceso"].tolist()
        aux = pd.DataFrame((zip(t, s)), columns = ['anio', 'casos'])
        dataX = aux[["anio"]]
        X_train = np.array(dataX)
        y_train = aux["casos"].values
        regr = linear_model.LinearRegression()
        regr.fit(X_train, y_train)
        y_pred = regr.predict(X_train)    
        prediccion = regr.predict([[2023]])
        return float(r2_score(y_train, y_pred)), float(prediccion)
       
        
   
