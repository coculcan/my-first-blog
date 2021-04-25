from django.http import HttpResponse

def index(request):
        return HttpResponse("Hola, mundo cruel")

# Create your views here.
