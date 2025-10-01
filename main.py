import requests

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=aa6f39da5592472a97d181851250110&q={city}&aqi=yes"

r = requests.get(url) # Sends HTTP GET request to the specified url; retrieves data from this REST API
print(r.text)
# print(type(r.text)) --> the type of r.text is string type



