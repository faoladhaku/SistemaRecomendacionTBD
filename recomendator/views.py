from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'recomendator/index.html')




##############################################
#### Algoritmos #############################






##############################################
def Controlador_respuesta(request):

	return render(request,'recomendator/Respuesta.html')
    