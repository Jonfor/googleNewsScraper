import requests
from bs4 import BeautifulSoup
#      https://www.google.com/search?q=tesla&biw=1440&bih=802&source=lnt&tbs=cdr%3A1%2Ccd_min%3A1%2F1%2F2013%2Ccd_max%3A1%2F5%2F2013&tbm=nws
URL = 'https://www.google.com/search?&q={query}&biw=1440&bih=802&source=lnt&tbs=cdr%3A1%2Ccd_min%3A1%2F1%2F{year}%2Ccd_max%3A1%2F5%2F{year}&tbm=nws'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}

def run(**params):
    response = requests.get(URL.format(**params), headers=headers)
    # 'https://www.google.com/search?&q=tesla&biw=1440&bih=802&source=lnt&tbs=cdr%3A1%2Ccd_min%3A1%2F1%2F2013%2Ccd_max%3A1%2F5%2F2013&tbm=nws'
    html_doc = response.content
    # FIND H3 TAGS WITH EITHER r OR _U6c CLASSES
    soup = BeautifulSoup(html_doc, 'html.parser')


if __name__ == "__main__":
    run(query="tesla", month=3, from_day=2, to_day=3, year=2013)
