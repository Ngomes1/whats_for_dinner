from django.shortcuts import render
from django.http import HttpResponse

def home():
    return HttpResponse("Are you looking for different recipes to try?? Look no further and enjoy these new meals!")

recipe = []

def random(request):
    if request.method == 'GET':
        return render(request, 'random.html', context = {'recipe':recipe})


