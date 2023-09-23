import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# Funcion para cargar datos de un CSV a una base de datos en MySQL 
def cargar_datos_desde_csv_mysql(host, usuario, contraseña, nombre_bd, archivo_csv, nombre_tabla):
    try:
        # Establecer la conexión a la base de datos MySQL utilizando SQLAlchemy
        engine = create_engine(f'mysql+mysqlconnector://{usuario}:{contraseña}@{host}/{nombre_bd}')

        # cargar el archivo CSV en un DataFrame de pandas
        df = pd.read_csv(archivo_csv)

        # Crear una tabla en la base de datos basada en el DataFrame
        df.to_sql(nombre_tabla, con=engine, if_exists='replace', index=False)

        # Mensaje informativo para confirmar que la carga de datos fue exitosa
        print(f"Datos cargados exitosamente desde '{archivo_csv}' a la tabla '{nombre_tabla}' en la base de datos '{nombre_bd}'.")

    except Exception as e:
        print(f'Error: {str(e)}')



cargar_datos_desde_csv_mysql('localhost', 'usuario', 'contraseña', 'criptomonedas', 'list_coins.csv', 'list_coins')        