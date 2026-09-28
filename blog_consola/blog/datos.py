perfil_autor = {
    'nombre': 'Ricardo Gutierrez.',
    'bio': 'Analista de datos y creador de contenido sobre programación.',
    'bspecialidad': 'Python, Django y PowerBi',
    'redes_sociales': ['@richard_data', '@richard_python', '@richard_aps']
}

estados_post = ('Borrador', 'Publicado', 'Archivado')
etiquetas_blog = {'Python', 'Django', 'Frontend', 'Backend', 'Data Analytics'}

posts = [
    {
        'id': 1,
        'titulo': 'Iniciando Python',
        'contenido': 'Aprende las bases de Python desde cero.',
        'autor': perfil_autor,
        'categoria': 'Programación',
        'tags': ['Python', 'Principiantes', 'Inicial'],
        'estado': 'Publicado'   
    },
    {
        'id': 2,
        'titulo': 'El Análisis de Datos',
        'contenido': 'Estrategias clave para ser analista.',
        'autor': perfil_autor,
        'categoria': 'Data',
        'tags': ['Python', 'Avanzados', 'Analista'],
        'estado': 'Borrador'   
    },
    {
        'id': 3,
        'titulo': '¡Hacelo más lindo con PowerBi!',
        'contenido': 'Dashboards interactivos en pocos pasos.',
        'autor': perfil_autor,
        'categoria': 'Visualización',
        'tags': ['Python', 'Avanzados', 'Interfaz'],
        'estado': 'Archivado'
    },
    
    {
        'id': 4,
        'titulo': '', 
        'autor': 'Ricardo', 
        'tags': 'Python', 
        'estado': 'Inexistente' 
    }
]