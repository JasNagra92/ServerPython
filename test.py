import requests

# Define the base URL of your API
base_url = 'http://localhost:5000'  # Update with your API's URL

# Define the endpoint URL
endpoint_url = f'{base_url}/api/data'  # Update with your specific API endpoint

# Send a GET request to the API endpoint
response = requests.get(endpoint_url)

# Check the response status code
if response.status_code == 200:
    # Request was successful
    data = response.json()
    print('Response Data:')
    print(data)
else:
    # Request failed
    print(f'Request failed with status code {response.status_code}')
    print(response.text)