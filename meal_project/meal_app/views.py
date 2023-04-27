from django.shortcuts import render
import requests
from .models import Meal

# Create your views here.

def get_meals(request):
    #create empty dictionary to hold all meals:
    all_meals = {}
    #check if the get request has a name in it:
    if 'name' in request.GET:
        name = request.GET['name']
        #from the API docs, get the url for the query:
        url ='https://www.themealdb.com/api/json/v1/1/search.php?s=%s' % name
        #create response object and convert to JSON:
        response = requests.get(url) #This is REQUESTS (plural, the library), NOT singular
        data = response.json()
        print(data)
        #Save the list generated in JSON file
        meals = data['meals']
        print(meals)

        #loop through json, equate model fields with json object values, and populate the database:
        for meal in meals:
            meal_data = Meal(
                name = meal['strMeal'],
                category = meal['strCategory'],
                instructions = meal['strInstructions'],
                yt_link = meal['strYoutube'],
                slug = meal['idMeal'],
                image_url = meal['strMealThumb'],
            )
            #save the data:
            meal_data.save()
            #retrieve all the meals and order by their id number from the database:
            all_meals = Meal.objects.all().order_by('id')

    return render(request, 'meal_app/meal.html', {'all_meals':all_meals})

def meal_detail(request):
    pass



#pip install requests (to build url that will connect to api)