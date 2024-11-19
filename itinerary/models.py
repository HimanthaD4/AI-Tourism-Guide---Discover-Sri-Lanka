from django.db import models


class DailyBudgetRange(models.Model):
    range_min = models.IntegerField()
    range_max = models.IntegerField()
    daily_budget = models.IntegerField()

    def __str__(self):
        return f"Daily Range {self.range_min} - {self.range_max}"


class Location(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    notes = models.TextField()

    def __str__(self):
        return self.name


class Activity(models.Model):
    location = models.ForeignKey(Location, related_name='activities', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(
        max_length=100,
        choices=[
            ('Cultural and Heritage Tours', 'Cultural and Heritage Tours'),
            ('Nature and Wildlife Tours', 'Nature and Wildlife Tours'),
            ('Beach and Coastal Tours', 'Beach and Coastal Tours'),
            ('Adventure Tours', 'Adventure Tours'),
            ('General', 'General')
        ]
    )
    price = models.IntegerField()
    image_url = models.URLField()
    description = models.TextField()
    activity_rank = models.PositiveIntegerField(default=1)
    price_range = models.CharField(max_length=50) 

    def __str__(self):
        return f"{self.name} - {self.category}"


class Route(models.Model):
    category = models.CharField(max_length=100)
    day_number = models.IntegerField()
    location = models.ForeignKey(Location, related_name='routes', on_delete=models.CASCADE)

    def __str__(self):
        return f"Day {self.day_number} - {self.category}"


class FoodCost(models.Model):
    daily_budget_range = models.ForeignKey(DailyBudgetRange, related_name='food_costs', on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f"Food Cost for Range {self.daily_budget_range.range_min} - {self.daily_budget_range.range_max}"
