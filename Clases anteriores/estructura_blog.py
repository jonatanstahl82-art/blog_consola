perfil_autor = {
        'Nombre': 'Ricardo Gutierrez.',
        'Bio': 'Analista de datos y creador de contenido sobre programación.',
        'Especialidad': 'Python, Django y PoweBi',
        'redes_sociales': ['@richard_data', '@richard_python', '@richard_aps']
}
estados_post = ('Borrador', 'Publicado', 'Archivado')
etiquetas_blog = {'Python', 'Django', 'Frontend', 'Backend', 'Data Analytics','Frontend','Python'}
Posts = [
        {
                'id': 1,
                'titulo': 'Iniciando Python',
                'autor': perfil_autor,
                'Categoria': 'Programación',
                'tags': ['Pyton', 'Principiantes', 'Inicial'],
                'estado': 'Publicado'   
        },
        {
                'id': 2,
                'titulo': 'El Analisis de Datos',
                'autor': perfil_autor,
                'Categoria': 'Data',
                'tags': ['Pyton', 'Avanzados', 'Analista'],
                'estado': 'Borrador'   
        },
        {
                'id': 3,
                'titulo': '¡Hacelo mas lindo con PowerBi!',
                'autor':  perfil_autor,
                'Categoria': 'Visualizacion',
                'tags': ['Python', 'Avanzados', 'Interfaz'],
                'estado': 'Archivado'
        }
]

print("Autor del segundo post:", Posts[1]["autor"]["Nombre"])
print("\nLista de posts guardados:\n")
print(Posts)