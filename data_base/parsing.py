import requests
from bs4 import BeautifulSoup

url = 'https://www.sports.ru/atletico/team/'


def sports_ru(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    table1 = soup.find('table', class_='stat-table sortable-table')
    tb = []
    headers = []
    for i in table1.find_all('span'):
        title = i.text
        headers.append(title)

    for j in table1.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        tb.append(row)
    return tb
