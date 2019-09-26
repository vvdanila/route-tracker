import datetime
import uuid
import json

from decimal import Decimal

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from geopy.distance import distance as geopy_distance

from route.models import Route, Point


@csrf_exempt
def create_route(request):

    if request.method == 'POST':
        route_id = str(uuid.uuid4())
        route = Route(route_id=route_id, creation_date=datetime.date.today())
        route.save()

        return JsonResponse({'route_id': route.route_id}, status=201)


@csrf_exempt
def add_way_point(request, route_id):
    def _compute_distance(point1, point2):
        point1 = (point1.latitude, point1.longitude)
        point2 = (point2.latitude, point2.longitude)
        return Decimal(geopy_distance(point1, point2).km)

    if request.method == 'POST':
        coordinates = json.loads(request.body.decode("utf-8"))

        if 'lat' not in coordinates or 'lon' not in coordinates:
            return JsonResponse('', status=400, safe=False)

        route = get_object_or_404(Route, route_id=route_id)

        if route.creation_date != datetime.date.today():
            return JsonResponse('', status=403, safe=False)

        previous_point = route.last_point

        point = Point(route=route, latitude=coordinates['lat'], longitude=coordinates['lon'])
        point.save()

        if previous_point:
            route.length += _compute_distance(previous_point, point)

        route.last_point = point
        route.save()

        return JsonResponse('', status=201, safe=False)


def calculate_length(request, route_id):
    route = get_object_or_404(Route, route_id=route_id)
    return JsonResponse({'km': float(route.length)}, status=200)
