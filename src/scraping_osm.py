import requests
import json

# Définition de la requête Overpass API
overpass_url = "http://overpass-api.de/api/interpreter"
query = """
[out:json];
area[name="Paris"]->.searchArea;
node["amenity"="hospital"](area.searchArea);
out body;
"""

# Exécuter la requête
response = requests.get(overpass_url, params={'data': query})
data = response.json()

# Sauvegarder les données
with open("data/hospitals_paris.json", "w") as f:
    json.dump(data, f, indent=4)

print("Scraping terminé, données sauvegardées !")