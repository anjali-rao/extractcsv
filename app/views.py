import pandas as pd

from django.shortcuts import render
from django.http.response import JsonResponse
from django.template import loader

def select_data(request):
    '''
    Renders page to select csv data file name and required fields
    '''
    filenames = ['file1.csv', 'file2.csv', 'file3.csv']
    fields = ['Sentiment', 'SentimentSource', 'SentimentText']
    context = dict(filenames=filenames, fields=fields)
    return render(request, 'select_data.html', context)

def get_data(request):
    '''
    On receiving the filename and fields from user,
    the appropriate data is selected from the data files
    available and provided to the user.
    '''
    filename = request.POST.get('filename', '')
    fields = request.POST.getlist('fields[]', '')
    csv_data = []
    with open('data/' + filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            csv_data.append([row[i] for i in fields])

    template = loader.get_template('csv_data.html')
    context = dict(csv_data=csv_data, fields=fields, success=True)
    html = template.render(context, request)

    return JsonResponse(dict(html=html, success=True))
