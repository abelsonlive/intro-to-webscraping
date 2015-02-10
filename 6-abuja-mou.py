import requests
from bs4 import BeautifulSoup
import csv

output_file = 'abuja-mou-data.csv'

url = 'http://abuja.marinet.ru/public.php/?action=getinsppublicall'

form = {
    'From': '01.01.2000',
    'To': '30.12.2014',
    'auth': '0',
    'flag': '0',
    'ShipClass': '0',
    'RoCode': '0',
    'Type': '0',
    'typeinspection': '1',
    'Ports': '0'
}

print "REQUESTING {}".format(form)
print "FROM {}".format(url)

r = requests.post(url, data=form)

soup = BeautifulSoup(r.content)

raw_rows = soup.find_all('tr', {'class': 'even'})
raw_rows.extend(soup.find_all('tr', {'class': 'odd'}))

data = []
for raw_row in raw_rows:
    clean_row = [] 
    idx = 0
    for cell in raw_row.find_all('td'):
        value = cell.text.strip()
        if value:
            clean_row.append(value)
    data.append(clean_row)

print "WRITING {} to file".format(output_file)
headers = [ 
    "date_of_inspection", "place_of_inspection", "name", 
    "call_sign", "flag", "imo", "deficiencies", "detained"
]

writer = csv.writer(open(output_file, 'wb'))
writer.writerow(headers)
writer.writerows(data)
