from django.urls import path

from route import views


urlpatterns = [
    path('', views.create_route, name='create_route'),
    path('<uuid:route_id>/way_point/', views.add_way_point, name='add_way_point'),
    path('<uuid:route_id>/length/', views.calculate_length, name='calculate_length'),
]
