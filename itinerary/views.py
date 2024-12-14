from django.shortcuts import render, redirect
from .models import Location, Activity, Route
from django.urls import reverse 
from datetime import datetime



def home(request): 
    return render(request, "home_page.html")





def travel_manage(request):
    if request.method == 'POST':
        landing_date = request.POST.get('landing_date')
        flying_date = request.POST.get('flying_date')
        budget = request.POST.get('budget')
        trip_type = request.POST.get('trip_type')
        food_priority = request.POST.get('food_priority')

        if landing_date and flying_date and budget and trip_type and food_priority:
            try:
                landing_date_obj = datetime.strptime(landing_date, '%Y-%m-%d')
                flying_date_obj = datetime.strptime(flying_date, '%Y-%m-%d')
                number_of_days = (flying_date_obj - landing_date_obj).days

                number_of_days = number_of_days - 1

                if number_of_days < 1 or number_of_days > 20:
                    return render(request, "travel_manage.html", {'error': 'Trip duration must be between 1 and 20 days.'})

                result_url = reverse('result', kwargs={
                    'number_of_days': number_of_days,
                    'budget': int(budget),
                    'trip_type': trip_type,
                    'food_priority': food_priority
                })
                return redirect(result_url)

            except ValueError:
                return render(request, "travel_manage.html", {'error': 'Invalid date format. Please use YYYY-MM-DD.'})

    return render(request, "travel_manage.html")


def result(request, number_of_days, budget, trip_type, food_priority):
    # Calculate food cost based on food priority
    food_cost_percentage = {'low': 0.10, 'medium': 0.30, 'high': 0.40}
    food_cost = (budget / number_of_days) * food_cost_percentage.get(food_priority, 0.30)
    remaining_budget = (budget / number_of_days) - food_cost
    daily_budget = budget / number_of_days

    # Retrieve all locations and filter activities based on trip_type
    locations = Location.objects.all()
    activities_by_location = {}

    # Filter activities by the selected trip_type
    for location in locations:
        location_activities = []
        for activity in location.activities.all():
            if activity.category == trip_type:  # Only include activities that match the trip_type
                location_activities.append(activity)
        if location_activities:  # Only add location if it has relevant activities
            activities_by_location[location] = location_activities

    context = {
        'number_of_days': number_of_days,
        'budget': budget,
        'trip_type': trip_type,
        'food_priority': food_priority,
        'food_cost': food_cost,
        'remaining_budget': remaining_budget,
        'daily_budget': daily_budget,
        'activities_by_location': activities_by_location
    }

    return render(request, 'result.html', context)