from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def homeview(request):
    context_shop = BMW.objects.all()
    if context_shop[0].islike == True:
        return redirect('juft')
    elif context_shop[0].islike == False:
        return redirect('toq')
    
    return render(request=request, template_name='index.html', context={})

def toq(request):
    return render(request, 'toq.html', context={})

def juft(request):
    return render(request, 'juft.html', context={})