import requests
from django.shortcuts import render

def home(request):
    weather_data = {}
    if request.method == "POST":
        # Get the city name from the form
        city = request.POST.get("city")
        if city:
            # Replace YOUR_API_KEY with your actual OpenWeatherMap API key
            api_key = "YOUR_API_KEY"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {"error": "City not found or API error."}
    return render(request, "forecast/home.html", {"weather_data": weather_data})
