from django.urls import path
from .views import *

urlpatterns = [
    path('', homeview),
    path('toq', toq, name='toq'),
    path('juft', juft, name='juft'),
]

