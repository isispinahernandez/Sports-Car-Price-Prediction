# Sports-Car-Price-Prediction
El objetivo de este repositorio es crear una aplicación con Streamlit para poder hacer la predicción del precio de un coche deportivo.

Realizado en Python 3.8

En este repositorio se puede encontrar:
 - Archivo "Sport car price.csv" contiene el dataset obtenido de https://www.kaggle.com/
 - Archivo "analisis.ipynb" contiene el análisis del dataset.
 - Archivo "main.py" contiene el código de ejecución de la applicación.
   (Recordar que para ejecutar este código hay que hacerlo mediante el comando:
    streamlit run main.py)
 - Carpeta "CarImagefolder" contiene las fotografías de los coches que se muestran 
 en la app.
  - El archivo "requirements.txt" te indica que requerimientos de las librerías son necesarias.
  - Necesitamos tener el archivo "model.pkl", ya que éste contiene el modelo de datos que analiza el precio del coche con los parametros seleccionados.

Cuando ejecutemos la app con el comando "streamlit run main.py" se nos muestra una ventana con el puerto "http://localhost:8501" que nos abre la aplicación y ya podemos realizar la predicción del precio para el coche deportivo deseado.

En la guia del usuario se puede encontrar el manual de uso para la applicación web.

TFM - ITTI | High TechInstitute
Profesor: José Manuel Peña Castro
