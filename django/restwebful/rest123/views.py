from .models import Drink
from rest_framework import viewsets
from .serilalizer import DrinkSerializer
from django.shortcuts import render


# Create your views here.

def home(request):
    context = {
        'drinks': Drink.objects.all()
    }
    return render(request, 'rest/index.html', context)

class DrinkViewSet(viewsets.ModelViewSet):
    '''
    API ENDPOINT
    '''
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
