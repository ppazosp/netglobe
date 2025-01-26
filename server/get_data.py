import requests

response = requests.get("https://restcountries.com/v3.1/all")
if response.status_code == 200:
    countries = response.json()
    for country in countries:
        name = country["name"]["common"]
        lat, lon = country["latlng"]
        print(f'{{"name":"{name}","latitude":"{lat}","longitude":"{lon}"}},')
else:
    print("Failed to fetch data")