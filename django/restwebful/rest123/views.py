from .models import Drink
from rest_framework import viewsets
from .serilalizer import DrinkSerializer
from django.shortcuts import render
import os
import slack
from dotenv import load_dotenv
from django.contrib import messages

load_dotenv()
client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))

# Create your views here.

def home(request):
    context = {
        'drinks': Drink.objects.all()
    }
    return render(request, 'rest/index.html', context)

def outofbeer(request):
    response = client.chat_postMessage(
        channel='#general',
        text="Saunatilasta on juomat loppu. Äkkiä lisää!")

    messages.success(request, 'Viesti lähetetty slack-kanavalle! Lisää olutta tulossa!')
    return render(request, 'rest/index.html')  

class DrinkViewSet(viewsets.ModelViewSet):
    '''
    API ENDPOINT
    '''
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer