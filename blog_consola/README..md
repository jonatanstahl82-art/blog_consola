## Blog por Consola - Organización modular ##

    Este proyecto se encarga de explorar los posts disponibles a través de un menú interactivo por consola. El archivo principal de ejecución es `main.py`.

## Como ejecutarlo:

    Desde la terminal, ubicado en la raíz del proyecto (`blog_consola/`), ejecutá:

        python main.py

La estructura del proyecto es la siguiente:

blog_consola/
│
├── main.py           # Punto de entrada y orquestador del programa
├── README.md         # Documentación del proyecto
│
└── blog/             # Paquete principal
    ├── __init__.py   # Reconocimiento de carpeta como paquete Python
    ├── datos.py      # Estructuras de datos base (posts, autores, estados)
    ├── validaciones.py # Reglas de validación lógica de estructuras
    ├── operaciones.py # Funciones de búsqueda y filtrado
    └── menu.py       # Menú interactivo y manejo de inputs de usuario


## Blog por Consola - Versión 1.4 (Modular, POO y Persistencia JSON)

Este proyecto es una aplicación de consola en Python diseñada para explorar, filtrar, validar y registrar publicaciones de un blog de forma interactiva. A partir de esta versión, el sistema incorpora **Programación Orientada a Objetos (POO)** y **persistencia de datos local mediante archivos JSON**.

El archivo principal de ejecución es `main.py`.

## Cómo ejecutarlo:

Desde la terminal, ubicado en la raíz del proyecto (`blog_consola/`), ejecutá:

    python main.py

## Estructura del proyecto:

blog_consola/
│
├── main.py              # Punto de entrada y orquestador del programa
├── README.md            # Documentación del proyecto
├── posts.json           # Archivo de persistencia local para los posts
│
└── blog/                # Paquete principal
    ├── __init__.py      # Inicialización y exportación de componentes
    ├── datos.py         # Estructuras de datos base e iniciales
    ├── modelos.py       # Clases del dominio (Post, autor)
    ├── validaciones.py  # Reglas de validación lógica de estructuras
    ├── operaciones.py   # Funciones de persistencia, búsqueda y filtrado
    └── menu.py          # Menú interactivo y manejo de inputs de usuario

## Novedades de la Versión 1.4:
- **Programación Orientada a Objetos (`modelos.py`)**: Definición de clases estructuradas para `Post` y `autor` con métodos de serialización a diccionarios (`to_dict()`).
- **Persistencia Local (`posts.json`)**: Capacidad de guardar automáticamente los nuevos posts creados por consola para mantener los datos de una ejecución a otra.
- **Validaciones Avanzadas (`validaciones.py`)**: Control exhaustivo de integridad sobre las claves, tipos de datos y estados permitidos de cada publicación.
- **Menú Interactivo Ampliado**: Nuevas opciones operativas para crear publicaciones y validar el estado de los datos en tiempo de ejecución.