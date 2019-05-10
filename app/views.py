import pandas as pd
import csv
from collections import defaultdict

from django.shortcuts import render
from django.http.response import JsonResponse
from django.template import loader

def select_data(request):
    filenames = ['file1.csv', 'file2.csv', 'file3.csv']
    fields = ['Sentiment', 'SentimentSource', 'SentimentText']
    context = dict(filenames=filenames, fields=fields)
    return render(request, 'select_data.html', context)

def get_data(request):
    filename = request.POST.get('filename', '')
    fields = request.POST.getlist('fields[]', '')
    csv_data = []
    with open('data/' + filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            csv_data.append([row[i] for i in fields])
    f.close()

    template = loader.get_template('csv_data.html')
    context = dict(csv_data=csv_data, fields=fields, success=True)
    html = template.render(context, request)

    columns = defaultdict(list) # each value in each column is appended to a list

    return JsonResponse(dict(html=html, success=True))
