import datetime
import json

from decimal import Decimal

from django.test import TestCase, Client

from route.models import Route


class RouteViewsTests(TestCase):
    client = Client()

    def test_create_route(self):
        response = self.client.post('/route/')

        assert 201 == response.status_code
        assert 'route_id' in response.json()

    def test_get_route_length_unsuccessful(self):
        response = self.client.get('/route/d214623e-94da-4789-9c4d-20d1f90aa908/length/')

        assert 404 == response.status_code

    def test_get_route_length_successful(self):
        route = Route(route_id='d214623e-94da-4789-9c4d-20d1f90aa908', creation_date=datetime.date.today(),
                      length=Decimal(20.25))
        route.save()

        response = self.client.get('/route/d214623e-94da-4789-9c4d-20d1f90aa908/length/')
        response_details = response.json()

        assert 200 == response.status_code
        assert 20.25 == response_details['km']

    def test_add_way_point_with_invalid_payload(self):
        response = self.client.post('/route/d214623e-94da-4789-9c4d-20d1f90aa908/way_point/',
                                    json.dumps({'lat': 25.25}),
                                    content_type="application/json")

        assert 400 == response.status_code

    def test_add_way_point_with_invalid_route(self):
        response = self.client.post('/route/d214623e-94da-4789-9c4d-20d1f90aa908/way_point/',
                                    json.dumps({'lat': 25.25, 'lon': 23.23}),
                                    content_type="application/json")

        assert 404 == response.status_code

    def test_add_way_point_successful(self):
        route = Route(route_id='d214623e-94da-4789-9c4d-20d1f90aa907', creation_date=datetime.date.today())
        route.save()

        response = self.client.post('/route/d214623e-94da-4789-9c4d-20d1f90aa907/way_point/',
                                    json.dumps({'lat': 25.25, 'lon': 23.23}),
                                    content_type="application/json")

        assert 201 == response.status_code
