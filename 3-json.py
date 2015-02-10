import requests
from pprint import pprint 

url = 'http://en.wikipedia.org/w/api.php'

search_parameters = {
    'action': 'opensearch',
    'limit': 10,
    'search': 'a'
}

response = requests.get(url, params=search_parameters)
pprint(response.json())