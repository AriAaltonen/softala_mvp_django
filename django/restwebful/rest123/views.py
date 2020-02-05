from .models import Drink
from rest_framework import viewsets
from .serilalizer import DrinkSerializer


# Create your views here.

class DrinkViewSet(viewsets.ModelViewSet):
    '''
    API ENDPOINT
    '''
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
