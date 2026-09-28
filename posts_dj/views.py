from django.http import HttpResponse

def inicio(request):
    return HttpResponse("¡Bienvenido al bolg!")

from django.http import HttpResponse

def lista_posts(request):
    return HttpResponse("Listado de posts del blog.")
