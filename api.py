import requests
import json

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/clear-address'

querystring = {
    'ipAddress': '118.25.6.39',
}

headers = {
    'Accept': 'application/json',
    'Key': 'YOUR_OWN_API_KEY'
}

response = requests.request(method='DELETE', url=url, headers=headers, params=querystring)

# Formatted output
decodedResponse = json.loads(response.text)
print(json.dumps(decodedResponse, sort_keys=True, indent=4))
