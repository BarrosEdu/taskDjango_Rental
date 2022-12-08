from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import json
from datetime import datetime

# Create your views here.

def reservation(request):

    df = pd.read_excel('./models/taskDjango.xlsx')

    df['Checkin'] = df['Checkin'].dt.strftime('%Y-%m-%d')
    df['Checkout'] = df['Checkout'].dt.strftime('%Y-%m-%d')

    json_records = df.reset_index().to_json(orient ='records')

    data = []
    data = json.loads(json_records)
    context = {'d': data}


    return render(request, 'reservation/reservation.html', context)