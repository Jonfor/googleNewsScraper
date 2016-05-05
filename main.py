try:
    import unicodecsv as csv
except ImportError:
    import warnings

    warnings.warn("can't import `unicodecsv` encoding errors may occur")
    import csv

import requests
from bs4 import BeautifulSoup

URL = 'https://www.google.com/search?&q={query}&biw=1440&bih=802&source=lnt&tbs=cdr%3A1%2Ccd_min%3A{month}%2F{from_day}%2F{year}%2Ccd_max%3A{month}%2F{to_day}%2F{year}&tbm=nws'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}

if __name__ == "__main__":

    endDay = 30
    tesla_csv = 'tesla.csv'
    with open(tesla_csv, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter="|")
        writer.writerow(['title', 'link', 'from_date', 'to_date'])
        for num in range(1, endDay):
            query = "tesla"
            month = 1
            from_day = num
            to_day = num
            year = 2013

            response = requests.get(URL.format(query="tesla", month=1, from_day=num, to_day=num, year=2013),
                                    headers=headers)
            html_doc = response.content
            soup = BeautifulSoup(html_doc, 'html.parser')
            for anchor in soup.find_all('h3'):
                for link in anchor.find_all('a'):
                    from_date = str(month) + '/' + str(from_day) + '/' + str(
                        year)
                    to_date = str(month) + '/' + str(to_day) + '/' + str(year)
                    writer.writerow([link.getText(), link.get('href'), from_date, to_date])
