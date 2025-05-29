# 🧠 Sistema de Monitoreo Ambiental

Este sistema permite simular la lectura de logs ambientales de distintas salas, almacenarlos temporalmente en una cache de tiempo configurable, realizar consultas dinámicas por sala o timestamp y generar reportes exportables en formatos CSV y XLSX.

---

## 📁 Estructura del Proyecto
.
├── main.py                   # Punto de entrada
├── cache.py                  # Cache temporal de logs
├── logs.py                   # Modelo de datos y parser CSV
├── utils.py                  # Funciones utilitarias (consultas y generación de logs)
├── reportes.py               # Estrategias para generación de reportes y exportación
├── requirements.txt          # Dependencias
├── .env                      # Variables de entorno (configuración)
├── logs_ambientales_ecowatch.csv
└── tests
    └── test_system.py  

## 🚀 Instalación y configuración

1. **Clonar el repositorio**  
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-repositorio>

2. **Crear y activar un entorno virtual**  
    (linux/mac)
    python3 -m venv venv
    source venv/bin/activate

    (windows)
    python -m venv venv
    .\venv\Scripts\activate

3. **Instalar dependencias** 
    pip install -r requirements.txt

4. **Configurar variables de entorno** 
    Crear un archivo .env en la raíz con las siguientes variables:
        DATA_SOURCE=logs_ambientales_ecowatch.csv
        CACHE_DURATION_MINUTES=5

5. **Ejecutar la aplicación** 
    python3 main.py


# 📦 Dependencias principales
pandas para manejo y análisis de datos.

python-dotenv para gestión de variables de entorno.  

# 📝 Uso principal

El sistema carga los logs desde un archivo CSV configurado en DATA_SOURCE 
(los carga en cache apenas se inicia, por eso si se ejecuta la opcion de Esperar 5 minutos y limpieza del cache pasados 5 minutos, la limpeza sera instantanea, sino se debera esperar lo que falte ).

Los logs se almacenan en una cache temporal con duración configurada por CACHE_DURATION_MINUTES.

Se pueden consultar logs en memoria por sala o timestamp.

Se generan reportes:

    Estado por sala: promedio de temperatura, humedad y CO2 por sala (exportado a CSV).

    Alertas críticas: logs con estado WARNING o niveles altos de CO2 (exportado a XLSX).


# 🔍 Análisis de diseño y decisiones técnicas

Estructuras de datos
    Uso de collections.deque para almacenamiento eficiente de logs temporales, permitiendo agregar y eliminar registros antiguos en tiempo constante.

    defaultdict de deque para agrupar logs por sala y consultas rápidas.

    dataclass para representar de forma clara y tipada cada log.

Patrones de diseño
    Factory: para instanciar el tipo de reporte deseado.

    Strategy: para encapsular la lógica específica de generación de reportes.

    Decorator: para añadir funcionalidades de exportación a distintos formatos (CSV, XLSX) sin modificar la lógica principal.

Optimización y prioridades
    Cache eficiente para evitar procesamiento innecesario.

    Consultas optimizadas por sala y timestamp.

    Modularidad y extensibilidad para facilitar mantenimiento y crecimiento.

    Legibilidad y separación clara de responsabilidades.


# 💡 Posibles mejoras futuras
Añadir soporte para nuevas fuentes de datos (APIs, bases de datos).

Implementar más tipos de reportes y filtros avanzados.

Interfaz web o API para consultas remotas.

Integración con alertas en tiempo real (email, SMS, etc.).


## 🧪 Pruebas unitarias

El proyecto incluye pruebas unitarias básicas para validar:

- El parseo correcto e incorrecto de logs CSV.

### Ejecutar pruebas

Para ejecutar las pruebas se utiliza el módulo `unittest` estándar de Python. Corre desde la raíz del proyecto:
    python -m unittest discover -s tests

¡Gracias por usar el sistema! Para cualquier duda o sugerencia, pedroseveri@gmail.com.