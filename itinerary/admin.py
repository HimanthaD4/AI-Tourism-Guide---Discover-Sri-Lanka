from django.contrib import admin
from .models import  DailyBudgetRange, Location, Activity, Route, FoodCost
from .models import Activity, Location

admin.site.register(DailyBudgetRange)
admin.site.register(Location)
admin.site.register(Activity)
admin.site.register(Route)
admin.site.register(FoodCost)
