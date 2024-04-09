
import requests
import json

key = "a86184fd83be486db83120827240904"

city = input("Enter the name of city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=a86184fd83be486db83120827240904&q={city}"

r = requests.get(url)
print(r.text)
print(type(r.text))