from random import sample

from django.http import HttpResponseServerError, HttpResponseNotFound, Http404
from django.shortcuts import render

from tours.data import departures, description, title, subtitle, tours


def main_view(request):
    random_tours = dict(sample(tours.items(), 6))
    return render(request, 'tours/index.html', context={
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'tours': random_tours
    })


def departure_view(request, departure_code):
    if departure_code not in departures:
        raise Http404('Такого нарпавления еще нет =(')
    dep_tours_dict = {}
    for tour_id, tour in tours.items():
        if departure_code == tour['departure']:
            dep_tours_dict[tour_id] = tour
    count_tours = len(dep_tours_dict)
    tour_dep = departures[departure_code]
    max_price = max(tour['price'] for tour in dep_tours_dict.values())
    min_price = min(tour['price'] for tour in dep_tours_dict.values())
    max_nights = max(tour['nights'] for tour in dep_tours_dict.values())
    min_nights = min(tour['nights'] for tour in dep_tours_dict.values())
    return render(request, 'tours/departure.html', context={
        'title': title,
        'tour_dep': tour_dep,
        'dep_tours_dict': dep_tours_dict,
        'count_tours': count_tours,
        'max_price': max_price,
        'min_price': min_price,
        'max_nights': max_nights,
        'min_nights': min_nights
    })


def tour_view(request, tour_id):
    try:
        tour = tours[tour_id]
    except KeyError:
        raise Http404('Тура с таким id еще нет =(')
    tour_dep_code = tour['departure']
    tour_dep = departures[tour_dep_code]
    return render(request, 'tours/tour.html', context={
        'title': title,
        'tour_id': tour_id,
        'tour': tour,
        'tour_dep': tour_dep,
    })


def custom_handler404(request, exception):
    return HttpResponseNotFound('<h2><b>404</b><br> Sorry, this page not found!</h2>')


def custom_handler500(request):
    return HttpResponseServerError('<h2><b>500</b><br> Sorry, server error!</h2>')
