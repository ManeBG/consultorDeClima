import requests  # Importa la librería requests para realizar la conexión con la API

# Definición de la función principal que consulta el clima
def get_weather(api_key, location_type, location):
    """
    Consulta el clima en OpenWeather según el tipo de ubicación (ciudad o coordenadas).
    Muestra el clima en caso de éxito o notifica al usuario de cualquier error.
    """
    try:
        # Construcción de la URL basada en el tipo de ubicación
        if location_type == 'city':
            # Desglosa la entrada para asegurar que el usuario siga el formato "CIUDAD,PAÍS"
            city, country = location.split(',')
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&lang=es&units=metric"
        elif location_type == 'coordinates':
            # Desglosa la entrada para latitud y longitud
            lat, lon = location.split(',')
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&lang=es&units=metric"
        else:
            # Levanta un error en caso de que el tipo de ubicación no sea válido
            raise ValueError("Tipo de ubicación no válido")

        # Realiza la solicitud GET y verifica errores HTTP
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción en caso de errores HTTP

        # Extrae el JSON de respuesta para obtener la descripción del clima
        data = response.json()
        # Verifica si la ciudad fue encontrada (OpenWeather devuelve "cod":200 para éxitos)
        if data.get("cod") != 200:
            raise ValueError("No se encontró la ciudad en OpenWeather")

        # Extrae y muestra la descripción del clima
        weather_description = data["weather"][0]["description"]
        city_name = data["name"]
        print(f"El clima en {city_name} es {weather_description}.")

    # Manejadores de errores específicos para informar al usuario
    except requests.exceptions.HTTPError as http_err:
        print(f"Error de HTTP: {http_err}")  # Notifica errores de HTTP al usuario
    except requests.exceptions.RequestException as req_err:
        print(f"Error al conectar con la API: {req_err}")  # Maneja errores de conexión
    except ValueError as val_err:
        print(f"Error en los datos ingresados: {val_err}")  # Informa errores en los datos del usuario
    except Exception as err:
        print(f"Error inesperado: {err}")  # Maneja cualquier otro error no anticipado

# Función principal para obtener datos del usuario y manejar el flujo de la aplicación
def main():
    # Solicita la clave API del usuario
    api_key = input("Introduce tu API key de OpenWeather: ")
    
    # Solicita al usuario el tipo de búsqueda (por ciudad o coordenadas) y convierte a minúsculas para consistencia
    location_type = input("¿Quieres consultar por ciudad o por coordenadas? (escribe 'city' o 'coordinates'): ").strip().lower()

    # Verifica el tipo de entrada y solicita los datos correspondientes
    if location_type == 'city':
        # El formato solicitado asegura la estructura que OpenWeather requiere
        location = input("Introduce la ciudad y el país en el formato 'CIUDAD,SIGLAS_DEL_PAÍS' (ej. 'Mexico City,MX'): ")
    elif location_type == 'coordinates':
        # El formato solicitado asegura la estructura necesaria para latitud y longitud
        location = input("Introduce la latitud y longitud en el formato 'LATITUD,LONGITUD' (ej. '19.4326,-99.1332'): ")
    else:
        # Si el usuario ingresa un tipo incorrecto, se informa y termina la ejecución
        print("Opción inválida, elige 'city' o 'coordinates'")
        return

    # Llama a la función get_weather para procesar los datos
    get_weather(api_key, location_type, location)

# Punto de entrada para la ejecución del script
if __name__ == "__main__":
    main()
