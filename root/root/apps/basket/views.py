from django.http import HttpResponse

def index(request):
    return HttpResponse("Successful ! <b>basket page !</b>")
