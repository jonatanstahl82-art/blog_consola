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