from decimal import Decimal

from django.db import models


class Route(models.Model):
    route_id = models.CharField(max_length=100, blank=False, unique=True)
    creation_date = models.DateField(blank=False)
    length = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=Decimal(0))
    last_point = models.ForeignKey('Point', related_name='last_point_on_route', null=True, blank=True, default=None,
                                   on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{}_{}'.format(self.route_id, self.length)


class Point(models.Model):
    route = models.ForeignKey(Route, on_delete=models.DO_NOTHING)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=False)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=False)

    def __str__(self):
        return '{}_{}_{}'.format(self.route.route_id, self.latitude, self.longitude)
