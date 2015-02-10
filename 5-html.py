import requests
from bs4 import BeautifulSoup

url = 'http://google.com/search'
search_parameters = {
    'q': 'hack the gibson'
}
response = requests.get(url, params=search_parameters)
soup = BeautifulSoup(response.content)

for search_result in soup.find_all('h3', {'class':'r'}):
    anchor_tag = search_result.find('a')
    raw_link = anchor_tag.attrs.get('href')
    clean_link = raw_link.split('q=')[-1]
    print clean_link
    

