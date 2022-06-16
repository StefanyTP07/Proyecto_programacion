import pandas as pd
'''
Crea diagrama de barras comparando los valores maximos por tipo de cada archivo de excel
Datos de entrada:
index: nombre de las columnas
maximos_bonilla: valores maximos de las columnas del archivo de bonilla
maximos_miraflores: valores maximos de las columnas del archivo de miraflores
unidad: unidad de las unidades representadas en los gráficos
'''
def barras_comparativas_max(index,maximos_bonilla,maximos_miraflores,unidad):
    df_comp=pd.DataFrame({'Bonilla': maximos_bonilla,'Ov.Miraflores': maximos_miraflores}, index=index)
    ax = df_comp.plot.bar(rot=0,figsize=(10,10),layout=(1,1))
    ax.set_xlabel(unidad)
    ax.set_ylabel("cantidad")
    titulo="Materiales: "
    for i in index:
        titulo=titulo+i+","
    titulo=titulo[:-1]
    ax.set_title(titulo)

'''
Encuentra la fila donde ocurrio el valor maximo ubicado
Datos de entrada:
df: Dataframe donde buscar
maximo_buscado: valor maximo a encontrar(fila)
columna: En que columna buscar
Datos de salida:
idx: fila donde se ubica el valor maximo
'''

def encuentra_fila_max(df,maximo_buscado,columna):
    col=df.iloc[:, columna-1]
    for i in range(len(col)): 
        if maximo_buscado==col[i]: 
            idx=i
    return idx
    
@st.experimental_memo
def download_data():
  url = "https://drive.google.com/uc?id=17B8hm_07RhiLpL0GPhuvEQumycgzowez"
  output = 'data.csv'
  gdown.download(url,output, quiet= False)

download_data()    
    
@st.experimental_memo
def download2_data():
  url = "https://drive.google.com/uc?id=1vyN3cnVUN1aUbx_w_r3AiLXRtY4puhty"
  output = 'data2.csv'
  gdown.download(url,output, quiet= False)

download2_data()
df_bon = pd.read_csv(r'data.csv', sep=',', nrows=1000000, parse_dates=['Fecha', 'Longitud'], header= 0)#almacenar el primer excel bonilla en un df
df_mir = pd.read_csv(r'data2.csv', sep=',', nrows=1000000, parse_dates=['Fecha', 'Longitud'], header= 0) #almacenar el segundo excel miraflores en un df
columnas = df_bon.columns.values #Obtener el nombre de las columnas

#Separar las columnas para su mejor visualización
index1=(columnas[6:7])#CO
index2=(columnas[7:10])#H2S,NO2,O3
index3=(columnas[10:11])#PM10
index4=(columnas[11:13])#PM2.5,SO2

#Separar las columnas para su mejor visualización Bonilla
max_bonilla = df_bon.max()#Obtiene los valores máximos por cada columna
barra1_1=max_bonilla[6:7]#valor maximo CO
barra1_2=max_bonilla[7:10]#valor maximo H2S,NO2,O3
barra1_3=max_bonilla[10:11]#valor maximo PM10
barra1_4=max_bonilla[11:13]#valor maximo PM2.5,SO2

#Separar las columnas para su mejor visualización Miraflores
max_mir = df_mir.max()#Obtiene los valores máximos por cada columna
barra2_1=max_mir[6:7]#valor maximo CO
barra2_2=max_mir[7:10]#valor maximo H2S,NO2,O3
barra2_3=max_mir[10:11]#valor maximo PM10
barra2_4=max_mir[11:13]#valor maximo PM2.5,SO2


fila=encuentra_fila_max(df_bon,max_bonilla[6],7) # Ejemplo para encontrar el la fila del valor maximo de bonilla de CO
print(fila)
print(df_bon.iloc[fila]) 

#Grafico de barra comparativos entre valores maximos
barras_comparativas_max(index1,barra1_1,barra2_1,"ug/m3")
barras_comparativas_max(index2,barra1_2,barra2_2,"ug/m3")
barras_comparativas_max(index3,barra1_3,barra2_3,"ug/m3")
barras_comparativas_max(index4,barra1_4,barra2_4,"ug/m3")

