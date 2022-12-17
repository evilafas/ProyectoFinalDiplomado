from fastapi import FastAPI
from contratos import contratos
app = FastAPI(title="API", version="1.0.0")

c = contratos()

@app.get("/datos")
def get_datos(): 
    data = c.mostrarDatos()
    return data

@app.get("/entidades_departamento")
def get_entidades_departamento(): 
    data = c.entidades_departamento()
    return data

@app.get("/entidades_ciudad")
def get_entidades_ciudad(): 
    data = c.entidades_ciudad()
    return data

@app.get("/media_precio_base")
def get_media_precio_base(): 
    data = c.media_precio_base()
    return data

@app.get("/modalidad_contratos")
def get_modalidad_contratos(): 
    data = c.modalidad_contratos()
    return data

@app.get("/tipo_contratos")
def get_tipo_contratos(): 
    data = c.tipos_contratos()
    return data

@app.get("/estado")
def get_estado(): 
    data = c.estado()
    return data

@app.get("/costos_año")
def get_costos_año(): 
    data = c.costos_año()
    return data

@app.get("/estado_procedimiento")
def get_estado_procedimiento(): 
    data = c.estado_procedimiento()
    return data

@app.get("/procesos_departamentos")
def get_procesos_departamentos(): 
    data = c.procesos_departamentos()
    return data

@app.get("/prediccion")
def get_prediccion(): 
    data = c.prediccionAnios()
    return data