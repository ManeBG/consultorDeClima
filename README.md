# Consultor de Clima con OpenWeather API

Este proyecto es un consultor de clima en Python que permite a los usuarios consultar el clima actual en una ciudad específica o mediante coordenadas (latitud y longitud), usando la API de OpenWeather.

## Descripción 

El consultor solicita al usuario si quiere buscar el clima en una ciudad (en formato CIUDAD,SIGLAS_DEL_PAÍS) o mediante coordenadas (LATITUD,LONGITUD). Luego, usa la API de OpenWeather para obtener el clima y muestra una breve descripción del mismo. Este proyecto está diseñado con un enfoque en el manejo robusto de errores para mejorar la experiencia del usuario y gestionar posibles problemas de conexión, formato incorrecto o datos no válidos.
Características 

    Consulta el clima mediante el nombre de la ciudad o por coordenadas.
    Manejo de errores para:
        Clave API incorrecta o no ingresada.
        Conexión a la API fallida.
        Datos mal ingresados por el usuario.
        Ciudad o coordenadas no encontradas en OpenWeather.
    Mensajes claros al usuario en caso de errores.
    Soporte para mensajes de clima en español.

Requisitos 

    Python 3.6 o superior
    Librería requests (puedes instalarla con pip install requests)
    API key de OpenWeather

Instalación y Ejecución 🚀

    Clona este repositorio:

    bash

git clone https://github.com/tu_usuario/consultor-de-clima.git
cd consultor-de-clima

Instala la librería requests:

bash

pip install requests

Ejecuta el script:

bash

    python consultor_clima.py

    Proporciona los datos requeridos:
        API key de OpenWeather.
        Ciudad y país (en formato CIUDAD,SIGLAS_DEL_PAÍS) o coordenadas (en formato LATITUD,LONGITUD).

#### Ejemplo de Uso 📌

bash

Introduce tu API key de OpenWeather: tu_api_key_aqui
¿Quieres consultar por ciudad o por coordenadas? (escribe 'city' o 'coordinates'): city
Introduce la ciudad y el país en el formato 'CIUDAD,SIGLAS_DEL_PAÍS' (ej. 'Mexico City,MX'): Mexico City,MX
El clima en Mexico City es muy nuboso.

Estructura del Código 📂

    consultor_clima.py: Contiene la lógica principal para consultar el clima y manejar errores de entrada y conexión.
    README.md: Documento explicativo del proyecto y su funcionamiento.

Buenas Prácticas Implementadas 🌟

    Manejo de errores detallado: Se manejan errores HTTP, errores en los datos del usuario y problemas de conexión.
    Validación de entrada: Permite solo formatos válidos, lo que mejora la precisión de los resultados.
    Modularidad: La función principal main() permite que el código sea fácil de ampliar o modificar.

Fuentes y Recursos 🌐

    Documentación de OpenWeather API
    Coordenadas GPS – Puedes usar esta página para encontrar las coordenadas de una ciudad.

Licencia 📄

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.