from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Portfolio</h1><p>Em construção...</p>")