from django.shortcuts import render
# from django.http import HttpResponse
# def index(request):
    # return HttpResponse("<h1>Hello, World!</h1>")
 
# Create your views here.

    
def index(request):
    msg = '<h1>This is Message from views</h1>'
    return render(request, 'home/index.html', {"message" : msg})

