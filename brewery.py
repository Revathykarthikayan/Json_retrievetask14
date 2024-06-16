import requests
import json


base_url = "https://api.openbrewerydb.org/breweries"


states = ["Alaska", "Maine", "New York"]
state_brewery_counts = {}

for state in states:
  url = f"{base_url}?by_state={state}"

  try:
    
    response = requests.get(url)
    response.raise_for_status()  

    breweries = json.loads(response.text)

    print(f"\nBreweries in {state}:")
    for brewery in breweries:
      name = brewery.get("name", "N/A")
      print(f"  - Name of the brewery: {name}")
    brewery_count = len(breweries)
    state_brewery_counts[state] = brewery_count
    for state, count in state_brewery_counts.items():
        print(f"Number of breweries in {state}: {count}")

    
  except requests.exceptions.RequestException as e:
    print(f"Error fetching breweries for state {state}: {e}")

    

    
