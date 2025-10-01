import requests
import json

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=aa6f39da5592472a97d181851250110&q={city}&aqi=yes"

r = requests.get(url) # Sends HTTP GET request to the specified url; retrieves data from this REST API
# print(r.text) --> prints the response body as a string
# The above line prints all the details of any city entered as input
# print(type(r.text)) --> the type of r.text is string type

weatherDict = json.loads(r.text)
# The json.loads() function is used to parse a JSON-formatted string and convert it into a Python object (dictionary, lists etc.)
w = weatherDict["current"]["temp_c"]
h = weatherDict["current"]["humidity"]

print(f"The temperature at {city} is: ", w, "degrees Celsius")
print(f"The humidity at {city} is: ", h )

