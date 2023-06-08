from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is home page")
    context = {
        "variable1" : "this is Great",
        "variable2" : "I am enjoying this"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")

def Contact(request):

    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")