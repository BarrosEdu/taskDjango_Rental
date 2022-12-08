from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import json
from datetime import datetime
import sqlite3

# Create your views here.

def reservation(request):

    # Conect with sqlite
    conn = sqlite3.connect('rental/db.sqlite3')

    #Read data and transform in DataFrame
    df = pd.read_sql('SELECT * from reservation',conn)

    json_records = df.reset_index().to_json(orient ='records')

    data = []
    data = json.loads(json_records)
    context = {'d': data}

    conn.close()

    return render(request, 'reservation/reservation.html', context)

