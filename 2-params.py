import requests

url = 'http://google.com/search'
search_parameters = {
    'q': 'hack the gibson'
}
response = requests.get(url, params=search_parameters)
print response.content
