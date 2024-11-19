from django.shortcuts import render, redirect
from .models import Location, Activity, Route, DailyBudgetRange, FoodCost
from django.urls import reverse 
from datetime import datetime


def home(request): 
    return render(request, "home_page.html")


def calculate_days(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    delta = end - start
    return delta.days + 1


def get_daily_budget_range(daily_budget):
    ranges = DailyBudgetRange.objects.filter(range_min__lte=daily_budget, range_max__gte=daily_budget).order_by('range_min')
    if ranges:
        return ranges[0]
    return None


def travel_manage(request):
    if request.method == "POST":
        landing_date = request.POST.get("landing_date")
        flying_date = request.POST.get("flying_date")
        budget = int(request.POST.get("budget"))
        trip_type = request.POST.get("trip_type")
        food_priority = request.POST.get("food_priority")

        # Calculate number of effective travel days (excluding landing and flying dates)
        landing_date = datetime.strptime(landing_date, "%Y-%m-%d")
        flying_date = datetime.strptime(flying_date, "%Y-%m-%d")
        number_of_days = max(1, (flying_date - landing_date).days - 1)

        # Redirect to the result view with the required parameters
        return redirect(reverse("result", args=[number_of_days, budget, trip_type, food_priority]))

    return render(request, "travel_manage.html")


def result(request, number_of_days, budget, trip_type, food_priority):
    adjusted_days = number_of_days
    daily_budget = budget / adjusted_days if adjusted_days > 0 else 0

    food_cost_percentage = {
        'low': 0.1,
        'medium': 0.3,
        'high': 0.4
    }.get(food_priority, 0)

    food_cost = daily_budget * food_cost_percentage
    remaining_budget = daily_budget - food_cost

    activities_by_category = {}
    categories = ['Jetwing', 'Authentic Ceylon', 'Adventure Spirit', 'Barefoot Luxury', 'General']
    for category in categories:
        activities = Activity.objects.filter(category=category)
        activities_by_category[category] = activities

    context = {
        'number_of_days': adjusted_days,
        'budget': budget,
        'daily_budget': daily_budget,
        'food_cost': food_cost,
        'remaining_budget': remaining_budget,
        'activities_by_category': activities_by_category,
        'trip_type': trip_type,
        'food_priority': food_priority,
    }
    return render(request, 'result.html', context)
