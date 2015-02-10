import requests

url = 'http://google.com/search?q=hack+the+gibson'
response = requests.get(url)
print response.content
