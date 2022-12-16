import dask.dataframe as dd
import pandas as pd

data = dd.read_csv("database/dataset.csv",
                   dtype={
                       'Fecha de Publicacion (Fase Borrador)': 'object',
                       'Fecha de Publicacion (Fase Seleccion Precalificacion)': 'object',
                       'Fecha de Publicacion (Manifestacion de Interes)': 'object',
                       'Fecha de Publicacion (Fase Planeacion Precalificacion)': 'object',
                   })
panda_df = data.compute()
panda_df = panda_df.astype(str)
print(panda_df.shape)
