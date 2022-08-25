from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    print(request.method)
    print(request)
    print(request.user.email)
    return render(request, 'index.html')
