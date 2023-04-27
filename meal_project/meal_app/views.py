from django.shortcuts import render

# Create your views here.

def get_meals(request):
    return render(request, 'meal_app/meal.html')

def meal_detail(request):
    pass