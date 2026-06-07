# Ingest data from REST API and store in raw landing zone

# Import required libraries
import requests, json, os

# Create destination folder if it does not exist
os.makedirs('data/raw/api', exist_ok=True)

# Fetch user data from public REST API
r = requests.get('https://jsonplaceholder.typicode.com/users', timeout=30)

# Save API response into JSON file
with open('data/raw/api/users.json', 'w') as f:
    json.dump(r.json(), f)

# Log completion message
print('API ingested')
