from django.contrib import admin
from django.urls import path
from itinerary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('travel_manage/', views.travel_manage, name='travel_manage'),
    path('result/<int:number_of_days>/<int:budget>/<str:trip_type>/<str:food_priority>/', views.result, name='result'),
]
