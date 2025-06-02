import requests
import json

url = "https://andmed.stat.ee/api/v1/en/stat/LET300"
headers = {'Content-Type': 'application/json'}

payload = {
    "query": [
        {
            "code": "Leibkonnapea haridustase",
            "selection": {
                "filter": "item",
                "values": ["1", "2", "3", "4"]
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

# Save or parse the JSON-stat data
data = response.json()
