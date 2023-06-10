# se ejecuta con el comando: streamlit run main.py
# csv https://www.kaggle.com/datasets/rkiattisak/sports-car-prices-dataset
# jupyter del modelo: "Analisis.py"

# Importamos librerias
import pickle as pk
import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd

# Definimos los parámetros para añadir los desplegables
carmodel = {"Acura":['NSX'],
            "Alfa Romeo":['4C','4C Spider','Giulia Quadrifoglio'],
            "Aston Martin":["DB11","DBS Superleggera","Vantage"],
            "Audi":['R8','R8 Spyder','RS 3','RS 5','RS 5 Coupe','RS 6','RS 6 Avant',
                    'RS 7','RS 7 Sportback','RS3','RS5','RS5 Coupe','RS6','RS6 Avant','RS7',
                    'RS7 Sportback','S5','TT RS', 'TT RS Coupe'],
            "Bentley":['Continental GT','Continental GT Speed'],
            "BMW":['i8','M2','M2 Competition','M2 CS','M4','M4 Competition',
                   'M4 Coupe','M5','M5 Competition','M8','Z4 M40i','Z4 Roadster'],
            "Bugatti":['Chiron','Chiron Pur Sport','Chiron Super Sport 300+'],
            "Chevrolet":['Camaro','Camaro SS','Camaro SS 1LE','Camaro SS Convertible',
                         'Camaro ZL1','Corvette','Corvette Stingray','Corvette Z06'],
            "Dodge":['Challenger','Challenger Hellcat','Challenger Hellcat Redeye',
                     'Challenger R/T','Challenger SRT Hellcat','Challenger SRT Hellcat Redeye',
                     'Charger','Charger Hellcat','Charger SRT Hellcat','Viper','Viper ACR'],
            "Ferrari":['488 GTB','812 Superfast','F8 Spider','F8 Tributo','Portofino',
                       'Portofino M','Roma','SF90 Stradale'],
            "Ford":['GT','Mustang','Mustang GT','Mustang Mach 1',
                    'Mustang Shelby GT500'],
            "Jaguar":['F-Type','F-Type R'],
            "Koenigsegg":['Jesko','Jesko Absolut'],
            "Lamborghini":['Aventador','Aventador S','Aventador SVJ','Huracan',
                           'Sián','Urus'],
            "Lexus":['LC',"LC 500"],
            "Lotus":['Evija','Evora','Evora GT'],
            "Maserati":['GranTurismo','MC20'],
            "McLaren":['570S','570S Spider','600LT','600LT Spider','720S',
                       '765LT','Artura','GT','Senna','Speedtail'], 
            "Mercedes-Benz":['AMG A45','AMG C 63','AMG C 63 S','AMG C43 Coupe','AMG C63',
                             'AMG GT','AMG GT 4-Door Coupe','AMG GT 63 S','AMG GT Black Series',
                             'AMG GT R','C 63 AMG','C63 AMG','C63 S AMG','CLS63 AMG','GT 63',
                             'S63 AMG','SL','SL 63 AMG','SLC 43','SLS AMG'],
            "Nissan":['370Z','370Z Coupe','370Z Nismo','400Z','GT-R Nismo'],
            "Pagani":['Huayra','Huayra BC','Huayra Roadster BC'],
            "Porche":['911','718 Boxster','718 Cayman','718 Cayman GT4','911 Turbo S',
                      '918 Spyder','Boxster','Cayman','Cayman GT4','Panamera','Panamera GTS',
                      'Panamera Turbo','Panamera Turbo S','Panamera Turbo S E-Hybrid',
                      'Taycan','Taycan 4S','Taycan Turbo S'],
            "Rimac":["C_Two","Nevera"],          
            "Rolls-Royce":["Dawn","Ghost","Wraith"],
            "Tesla":["Model S","Model S Plaid","Roadster"]}

# Imágenes                  
image= {"Acura":'./CarImagefolder/acura-nsx.jpg',
        "Alfa Romeo":'./CarImagefolder/alfa_romeo_4cspider.jpg',
        "Aston Martin":'./CarImagefolder/Aston_Martin_DB11.jpg',
        "Audi":'./CarImagefolder/audi-rs5-coupe.webp',
        "Bentley":'./CarImagefolder/Bentley_Continental_GTspeed.png',
        "BMW":'./CarImagefolder/bmwz4.jpg',
        "Bugatti":'./CarImagefolder/bugattichiron.webp' ,
        "Chevrolet":'./CarImagefolder/chevrolet_corvette.JPG',
        "Dodge":'./CarImagefolder/dodge-viper.jpg',
        "Ferrari":'./CarImagefolder/ferrari-roma.jpg',
        "Ford":'./CarImagefolder/ford-mustang.webp',
        "Jaguar":'./CarImagefolder/jaguar-f-type.jpg',
        "Koenigsegg":'./CarImagefolder/Koenigseggjesko.jpg',
        "Lamborghini":'./CarImagefolder/lamborghini-sian.jpg',
        "Lexus":'./CarImagefolder/Lexus-LC_500.webp',
        "Lotus":'./CarImagefolder/lotus-evora.jpg',
        "Maserati":'./CarImagefolder/maseratigranturismo.jpg',
        "McLaren":'./CarImagefolder/McLaren_570s_spider.jpg',
        "Mercedes-Benz":'./CarImagefolder/merdecesamg.jpg',
        "Nissan":'./CarImagefolder/nissan-370z.webp',
        "Pagani":'./CarImagefolder/pagani-huayra-roadster.jpg',
        "Porche":"./CarImagefolder/porsche-panamera-gts.jpg",
        "Rimac":'./CarImagefolder/rimac-c_two.jpg',
        "Rolls-Royce":'./CarImagefolder/Rolls-Royce-Dawn.jpg',
        "Tesla":'./CarImagefolder/tesla-roadster.jpg' }

# Configuramos página
st.set_page_config(page_title="Sport Car Predict", layout="wide")

# Título
st.markdown("<h1 style='text-align: center; color: orange;'> Coches Deportivos</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>(Estimador de Precios) </h4>", unsafe_allow_html=True)
st.title("")

# Capturamos las variables para hacer la predicción
col1, col2 = st.columns(2)
with col1:
   # Selección de la marca coche 
   opcion = st.selectbox("**:violet[Selecciona la marca del coche (ordenados alfabéticamente): ]**",
                       carmodel.keys())
   st.write("**:black[Has elegido: ]**", opcion)

with col2:
   # Añadimos la imagen de uno de los modelos de la marca escogida
   for k in image:
    if opcion == k:
        Carimage = Image.open(image[k])
        st.image(Carimage, caption= opcion)

col3, col4 = st.columns(2)
with col4:
    # Selección del modelo del coche
    for k in carmodel:
        if opcion == k:
            radio = st.radio(("**:violet[Los modelos posibles a la marca elegida son:]**"),
                         carmodel[k])
with col3:
    # Año del coche
    year = st.selectbox("**:violet[Selecciona el año del coche:]**",
                      ("2020","2021","2022"))
    st.write("**:black[Año seleccionado:]**", year) 

    # Selección del tiempo de acceleración
    acctime = st.radio(("**:violet[Elige el intervalo de tiempos de aceleración (0s-60s) que quieres que tenga tu coche:]**"),
                         ("De 0s a 2s","De 2s a 2.5s","De 2.5s a 3s","De 3s a 3.5s",
                          "De 3.5s a 3.8s","De 3.8s a 4s","Mas de 4s"))
    # Convertimos el valor que nos da el usuario a valor de predicción
    if acctime =='De 0s a 2s':
        Time0to60 = 0
    elif acctime =='De 2s a 2.5s':
        Time0to60 = 1
    elif acctime =='De 2.5s a 3s':
        Time0to60 = 2
    elif acctime =='De 3s a 3.5s':
        Time0to60 = 3
    elif acctime =='De 3.5s a 3.8s':
        Time0to60 = 4
    elif acctime =='De 3.8s a 4s':
        Time0to60 = 5
    elif acctime =='Mas de 4s':
        Time0to60 = 6
st.write(" ")
st.write(" ")

# Horsepower
Hp = st.slider("**:violet[Que rango de potencia del motor (caballos) quieres que tenga?]**", 
                  181., 1479., (400.0, 700.0))
st.write("**:black[Intervalo seleccionado:]**", Hp)
# Igual que con el tiempo convertimos el valor que nos da el usuario a valor de predicción
if Hp[1] <= 200:
    Hpower = '0'
elif Hp[1] <= 400:
    Hpower = '1'
elif Hp[1] <= 500:
    Hpower = '2'
elif Hp[1] <= 600:
    Hpower = '3'
elif Hp[1] <= 700:
    Hpower = '4'
elif Hp[1] <= 750:
    Hpower = '5'
else:
    Hpower = '6'

if Hpower == '0':
    st.write("**:black[El valor máximo que tendremos en cuenta para el cálculo del precio es 200]**")
elif Hpower == '1':
    st.write("**:black[El valor máximo que tendremos en cuenta para el cálculo del precio es 400]**")
elif Hpower == '2':
    st.write("**:black[El valor máximo que tendremos en cuenta para el cálculo del precio es 500]**")
elif Hpower == '3':
    st.write("**:black[El valor máximo que tendremos en cuenta para el cálculo del precio es 600]**")
elif Hpower == '4':
    st.write("**:black[El valor máximo que tendremos en cuenta para el cálculo del precio es 700]**")
elif Hpower == '5':
    st.write("**:black[El valor máximo que tendremos en cuenta para el cálculo del precio es 750]**")
else:
    st.write("**:black[El valor máximo que tendremos en cuenta para el cálculo del precio es:]**",Hp[1])

# Selección del color: no nos aporta información para el modelo 
# ya que no es variable de predicción pero el usuario puede elegir 
# multiples opciones 
colours = st.multiselect("**:violet[Finalmente, indica si tienes alguna preferencias de color]**(Selecciona todos los que desees)",
                         ["Blanco","Negro","Gris","Rojo","Amarillo","Azul","Verde Aceituna","NA"])
st.write("**:black[Has elegido los siguientes colores:]**", colours)

# Con la información introducida por el usuario creamos el array 
# para los datos correspondientes a realizar el calculo del modelo

varstreamlit=[year,Hpower,Time0to60]
marca= 'Car_Make_'+opcion
modelo= 'Car_Model_'+radio

varmodel= ["Year","Horsepower","Time0to60","Car_Make_Acura","Car_Make_Alfa Romeo",
      "Car_Make_Alpine","Car_Make_Ariel","Car_Make_Aston Martin","Car_Make_Audi",
      'Car_Make_BMW','Car_Make_Bentley','Car_Make_Bugatti','Car_Make_Chevrolet',
      'Car_Make_Dodge','Car_Make_Ferrari','Car_Make_Ford','Car_Make_Jaguar',
      'Car_Make_Kia','Car_Make_Koenigsegg','Car_Make_Lamborghini','Car_Make_Lexus',
      'Car_Make_Lotus','Car_Make_Maserati','Car_Make_Mazda','Car_Make_McLaren',
      'Car_Make_Mercedes-AMG','Car_Make_Mercedes-Benz','Car_Make_Nissan','Car_Make_Pagani',
      'Car_Make_Pininfarina','Car_Make_Polestar','Car_Make_Porsche','Car_Make_Rimac',
      'Car_Make_Rolls-Royce','Car_Make_Shelby','Car_Make_Subaru','Car_Make_TVR',
      'Car_Make_Tesla','Car_Make_Toyota', 'Car_Make_Ultima','Car_Make_W Motors',
      'Car_Model_1','Car_Model_370Z','Car_Model_370Z Coupe','Car_Model_370Z Nismo',
      'Car_Model_400Z','Car_Model_488 GTB','Car_Model_4C','Car_Model_4C Spider', 
      'Car_Model_570S','Car_Model_570S Spider','Car_Model_600LT','Car_Model_600LT Spider',
      'Car_Model_718 Boxster','Car_Model_718 Cayman','Car_Model_718 Cayman GT4',
      'Car_Model_720S','Car_Model_765LT','Car_Model_812 Superfast', 'Car_Model_911',
      'Car_Model_911 Turbo S','Car_Model_918 Spyder','Car_Model_A110','Car_Model_AMG A45',
      'Car_Model_AMG C 63','Car_Model_AMG C 63 S','Car_Model_AMG C43 Coupe',
      'Car_Model_AMG C63','Car_Model_AMG GT','Car_Model_AMG GT 4-Door Coupe',
      'Car_Model_AMG GT 63 S','Car_Model_AMG GT Black Series','Car_Model_AMG GT R',
      'Car_Model_Artura','Car_Model_Atom','Car_Model_Aventador','Car_Model_Aventador S',
      'Car_Model_Aventador SVJ','Car_Model_Battista','Car_Model_Boxster',
      'Car_Model_C 63 AMG','Car_Model_C 63 S','Car_Model_C 63 S Coupe','Car_Model_C63 AMG',
      'Car_Model_C63 S','Car_Model_C63 S AMG','Car_Model_C63 S Coupe','Car_Model_CLS63 AMG',
      'Car_Model_C_Two','Car_Model_Camaro','Car_Model_Camaro SS','Car_Model_Camaro SS 1LE',
      'Car_Model_Camaro SS Convertible','Car_Model_Camaro ZL1','Car_Model_Cayman',
      'Car_Model_Cayman GT4','Car_Model_Challenger','Car_Model_Challenger Hellcat',
      'Car_Model_Challenger Hellcat Redeye','Car_Model_Challenger R/T',
      'Car_Model_Challenger SRT Hellcat','Car_Model_Challenger SRT Hellcat Redeye',
      'Car_Model_Charger','Car_Model_Charger Hellcat','Car_Model_Charger SRT Hellcat',
      'Car_Model_Chiron','Car_Model_Chiron Pur Sport','Car_Model_Chiron Super Sport 300+',
      'Car_Model_Cobra','Car_Model_Continental GT','Car_Model_Continental GT Speed',
      'Car_Model_Corvette','Car_Model_Corvette Stingray','Car_Model_Corvette Z06',
      'Car_Model_DB11','Car_Model_DBS Superleggera','Car_Model_Dawn','Car_Model_Evija',
      'Car_Model_Evora','Car_Model_Evora GT','Car_Model_F-Type','Car_Model_F-Type R',
      'Car_Model_F8 Spider','Car_Model_F8 Tributo','Car_Model_Fenyr SuperSport',
      'Car_Model_Fenyr Supersport','Car_Model_GR Supra','Car_Model_GT','Car_Model_GT 63',
      'Car_Model_GT 63 S','Car_Model_GT Black Series','Car_Model_GT-R Nismo',
      'Car_Model_Ghost','Car_Model_Giulia Quadrifoglio','Car_Model_GranTurismo',
      'Car_Model_Griffith','Car_Model_Huayra','Car_Model_Huayra BC',
      'Car_Model_Huayra Roadster BC', 'Car_Model_Huracan','Car_Model_Jesko',
      'Car_Model_Jesko Absolut','Car_Model_LC','Car_Model_LC 500',
      'Car_Model_Lykan Hypersport','Car_Model_M2','Car_Model_M2 CS',
      'Car_Model_M2 Competition','Car_Model_M4','Car_Model_M4 Competition',
      'Car_Model_M4 Coupe','Car_Model_M5','Car_Model_M5 Competition','Car_Model_M8',
      'Car_Model_MC20','Car_Model_MX-5 Miata','Car_Model_Model S','Car_Model_Model S Plaid',
      'Car_Model_Mustang','Car_Model_Mustang GT','Car_Model_Mustang Mach 1',
      'Car_Model_Mustang Shelby GT500','Car_Model_NSX','Car_Model_Nevera',
      'Car_Model_Panamera','Car_Model_Panamera GTS','Car_Model_Panamera Turbo',
      'Car_Model_Panamera Turbo S','Car_Model_Panamera Turbo S E-Hybrid','Car_Model_Portofino',
      'Car_Model_Portofino M','Car_Model_R8','Car_Model_R8 Spyder','Car_Model_RS',
      'Car_Model_RS 3','Car_Model_RS 5','Car_Model_RS 5 Coupe','Car_Model_RS 6',
      'Car_Model_RS 6 Avant','Car_Model_RS 7','Car_Model_RS 7 Sportback',
      'Car_Model_RS3','Car_Model_RS5','Car_Model_RS5 Coupe','Car_Model_RS6',
      'Car_Model_RS6 Avant','Car_Model_RS7','Car_Model_RS7 Sportback','Car_Model_Roadster',
      'Car_Model_Roma','Car_Model_S5','Car_Model_S63 AMG','Car_Model_SF90 Stradale',
      'Car_Model_SL','Car_Model_SL 63 AMG','Car_Model_SLC 43','Car_Model_SLS AMG',
      'Car_Model_SLS AMG Black Series','Car_Model_Senna','Car_Model_Sián',
      'Car_Model_Speedtail','Car_Model_Stinger','Car_Model_Supra','Car_Model_TT RS',
      'Car_Model_TT RS Coupe','Car_Model_Taycan','Car_Model_Taycan 4S',
      'Car_Model_Taycan Turbo S','Car_Model_Urus','Car_Model_Vantage','Car_Model_Viper',
      'Car_Model_Viper ACR','Car_Model_WRX STI','Car_Model_Wraith','Car_Model_Z4 M40i',
      'Car_Model_Z4 Roadster','Car_Model_i8']

for i in range(3,len(varmodel),1):
    if (varmodel[i] == marca) or (varmodel[i] == modelo):
        varstreamlit.append(1)
    else:
        varstreamlit.append(0)

# Declaramos la función que predice el modelo
def modelpred():
    pred=pk.load(open('model.pkl','rb')).predict([varstreamlit])
    return pred

# Generamos el boton para que nos realice la predicción y
# nos indique el precio del coche elegido con las caracteristicas
# introducidas
if st.button("**:orange[Predecir Precio]**"):
    resultado = modelpred()
    st.write(":green[El precio del coche elegido es:]", int(resultado[0]),":green[dolares]")
st.write("\n")

# Haremos un grafico con el precio medio del modelo elegido
# Descargamos csv con los datos

datacsv = pd.read_csv("Sport car price.csv", sep= ",")
datacsv.rename(columns={'Car Make':'Car_Make','Car Model':'Car_Model','Engine Size (L)':'Engine_Size','Torque (lb-ft)':'Torque','0-60 MPH Time (seconds)':'Time0to60','Price (in USD)':'Price'}, inplace=True)
df = datacsv.drop(["Engine_Size"], axis = 1)
dfNew = df.drop(["Torque"], axis = 1)

for i in range(len(df)):
    if dfNew.Time0to60[i] <= '0':
        dfNew.Time0to60[i] = '0'
    elif dfNew.Time0to60[i]<= '2':
        dfNew.Time0to60[i] = 'up0to2'
    elif dfNew.Time0to60[i]<= '2.5':
        dfNew.Time0to60[i] = 'up2to2,5'
    elif dfNew.Time0to60[i]<= '3':
        dfNew.Time0to60[i] = 'up2,5to3'
    elif dfNew.Time0to60[i]<= '3.5':
        dfNew.Time0to60[i] = 'up3to3,5'
    elif dfNew.Time0to60[i]<= '3.8':
        dfNew.Time0to60[i] = 'up3,5to3,8'
    elif dfNew.Time0to60[i]<= '4':
        dfNew.Time0to60[i] = 'up3,8to4'
    else:
        dfNew.Time0to60[i] = 'up4'

for i in range(len(df)):
    if dfNew.Horsepower[i] <= '0':
        dfNew.Horsepower[i] = '0'
    elif dfNew.Horsepower[i]<= '200':
        dfNew.Horsepower[i] = 'up0to200'
    elif dfNew.Horsepower[i]<= '400':
        dfNew.Horsepower[i] = 'up200to400'
    elif dfNew.Horsepower[i]<= '500':
        dfNew.Horsepower[i] = 'up400to500'
    elif dfNew.Horsepower[i]<= '600':
        dfNew.Horsepower[i] = 'up500to600'
    elif dfNew.Horsepower[i]<= '700':
        dfNew.Horsepower[i] = 'up600to700'
    elif dfNew.Horsepower[i]<= '750':
        dfNew.Horsepower[i] = 'up700to750'
    else:
        dfNew.Horsepower[i] = 'up750'

dfNewcol = dfNew.drop(["Car_Model"], axis = 1)
dfNewcol = dfNewcol.drop(["Car_Make"], axis = 1)
dfNewcol = dfNewcol.drop(["Price"], axis = 1)
columns = tuple(dfNewcol.columns)
dfNew['Price'] = dfNew['Price'].str.replace(",", "")
dfNew['Price'] = dfNew['Price'].astype(str).astype(int)

# Buscamos el modelo elegido
for car in carmodel:
    if opcion == car:
        dfN = dfNew[(dfNew['Car_Make'] == opcion) & (dfNew['Car_Model']== radio)]
        dfNew2 = dfNew[(dfNew['Car_Make'] == opcion)]
        H=dfNew2.groupby('Car_Model')['Price'].mean().sort_values(ascending=False)
        fig = px.bar( x = H.index, y = H,
                     labels={'x': 'Modelo', 'y': 'Precio medio'},
                     text_auto=True)
        fig.update_layout(title=dict(text=f"Precio medio de los coches de la marca {opcion}",
        font=dict(size=18), x=0.4))
        st.plotly_chart(fig, use_container_width=True)

        col5, col6 = st.columns(2)
        with col5:
            Cav=dfN.groupby('Horsepower')['Price'].mean().sort_values()
            fig = px.bar(dfN, x = Cav.index, y = Cav,
                             title=f"Precio medio de los {opcion}, modelo {radio} según los Caballos de Potencia",
                             labels={'x':'Caballos de potencia', 'y':'Precio medio'},
                             text_auto=True,
                          opacity=0.5,
                             width = 15,
                             color_discrete_sequence =['green'])
            st.plotly_chart(fig, use_container_width=True)
           
        with col6:
            T=dfN.groupby('Time0to60')['Price'].mean()
            fig = px.bar(dfN, x = T.index, y=T,
                             title=f"Precio medio de los {opcion}, modelo {radio} según el tiempo de accelarción",
                             labels={'x':'Aceleración de 0 a 60 seg', 'y':'Precio medio'},
                             text_auto=True,
                             opacity=0.5,
                             width = 15,
                             color_discrete_sequence =['green'])
            st.plotly_chart(fig, use_container_width=True)

dfPrice = dfNew[(dfNew['Price'] > 1000000)]
dfPrice2 = dfPrice[(dfPrice['Car_Make'] != "W Motors") & (dfPrice['Car_Make'] != "Pininfarina")]
Pr_C=dfPrice2.groupby('Car_Make')['Price'].mean().sort_values(ascending=False)
fig = px.funnel(dfPrice, x=Pr_C, y=Pr_C.index,
                opacity=0.9, color_discrete_sequence =['orange'],
                labels={'x':'Precio medio', 'y':'Marca'})
fig.update_traces(textfont = {'color': 'white'})
fig.update_layout(title=dict(text="Top Marcas con precio mayor a 1M dolares",
        font=dict(size=20), x=0.4))
st.plotly_chart(fig, use_container_width=True)

