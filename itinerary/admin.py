from django.contrib import admin
from .models import  Location, Activity, Route
from .models import Activity, Location


admin.site.register(Location)
admin.site.register(Activity)
admin.site.register(Route)

