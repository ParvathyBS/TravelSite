from django.http import HttpResponse
from django.shortcuts import render

from .models import Place
from .models import Team


# Create your views here.
# def home(request):
# return HttpResponse("Welcome to the home page")

def demo(request):
    obj = Place.objects.all()
    ob = Team.objects.all()
    return render(request, 'index.html', {'result': obj, 'result1': ob})
    # return render(request, 'index.html',{})

# def addition(request):
#   n1 = int(request.GET["number1"])
# n2 = int(request.GET["number2"])
#   Sum = n1 + n2
# return render(request,"home.html",{'s': Sum})

# def product(request):
#       n1 = int(request.GET["number1"])
#   n2 = int(request.GET["number2"])
#   pd = n1 * n2
#  return render(request, "product.html", {'p': pd})

# def difference(request):
#    n1 = int(request.GET["number1"])
#   n2 = int(request.GET["number2"])
#   di = n1 - n2
#   return render(request, "difference.html", {'d': di})

# def quotient(request):
#       n1 = int(request.GET["number1"])
#   n2 = int(request.GET["number2"])
#   qu = n1 / n2
#    return render(request, "quotient.html", {'q': qu})
