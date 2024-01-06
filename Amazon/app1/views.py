from django.shortcuts import render

# Create your views here.

def samplepage(request):
    return render (request, 'sample.html')
