try:
    import unicodecsv as csv
except ImportError:
    import warnings

    warnings.warn("can't import `unicodecsv` encoding errors may occur")
    import csv

import requests
from bs4 import BeautifulSoup

URL = 'https://www.google.com/search?&q={query}&biw=1440&bih=802&source=lnt&tbs=cdr%3A1%2Ccd_min%3A{month}%2F{from_day}%2F{year}%2Ccd_max%3A{month}%2F{to_day}%2F{year}&tbm=nws'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}


def run(**params):
    response = requests.get(URL.format(**params), headers=headers)

    html_doc = response.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    tesla_csv = 'tesla.csv'
    with open(tesla_csv, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter="|")
        writer.writerow(['title', 'link', 'from_date', 'to_date'])
        for anchor in soup.find_all('h3'):
            for link in anchor.find_all('a'):
                from_date = str(params.get('month')) + '/' + str(params.get('from_day')) + '/' + str(params.get('year'))
                to_date = str(params.get('month')) + '/' + str(params.get('to_day')) + '/' + str(params.get('year'))
                writer.writerow([link.getText(), link.get('href'), from_date, to_date])
                print(link.getText())

if __name__ == "__main__":
    run(query="tesla", month=1, from_day=1, to_day=5, year=2013)
