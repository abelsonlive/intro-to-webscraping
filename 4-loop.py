import requests
from pprint import pprint 

url = 'http://en.wikipedia.org/w/api.php'

search_parameters = {
    'action': 'opensearch',
    'limit': 10,
    'search': "",
}

queries = [
    'a','b','c','d','1','2','3','4'
]

results = []

for q in queries:
    print "searching for", q
    search_parameters['search'] = q 
    response = requests.get(url, params=search_parameters)
    data = response.json()
    results.append(data[1][1])
pprint(results)