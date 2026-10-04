class Post:
    def __init__(self, id, titulo, contenido, autor, categoria, tags, estado="Borrador"):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.categoria = categoria
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        """Pasa el objeto a diccionario para poder guardarlo en JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor,
            "categoria": self.categoria,
            "tags": self.tags,
            "estado": self.estado
        }

class autor:
    def __init__(self, nombre, bio):
        self.nombre = nombre
        self.bio = bio

    def to_dict(self):
        """Pasa el objeto a diccionario para poder guardarlo en JSON."""
        return {
            "nombre": self.nombre,
            "email": self.bio
        }
    