from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count

from .models import Passenger


def chart_data(request):
    data = Passenger.objects.values('embarked').exclude(embarked='').annotate(total=Count('embarked')).order_by('embarked')

    port_display_name = dict()
    for port_tuple in Passenger.PORT_CHOICES:
        port_display_name[port_tuple[0]] = port_tuple[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'series': [{
            'name': 'Embarkation Port',
            'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, data))
        }]
    }

    return JsonResponse(chart)


def charts(request):
    return render(request, 'charts.html')
