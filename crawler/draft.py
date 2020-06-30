import requests
import pandas as pd
import bs4
from bs4 import BeautifulSoup

#--- setup
url = "https://finviz.com/quote.ashx?t=FB"
def extract_source(url):
    agent = {"User-Agent": "Mozilla/5.0"}
    source = requests.get(url, headers=agent).text
    return source
source = extract_source(url)
soup = BeautifulSoup(source, 'lxml')

#--- news

# news table object
news_table = soup.find_all(id="news-table")[0]

# add rows
date = 'no date'
data = []
for tr in news_table:
    if isinstance(tr, bs4.element.Tag):
        timeinfo = tr.td.string.strip()
        if tr.find(style="white-space:nowrap"):  # top row of the date
            date, timestamp = timeinfo.split()
        else:
            timestamp = timeinfo
        news = tr.a.string
        row = [date, timestamp, news]
        data.append(row)
df = pd.DataFrame(data, columns=['Date','Time','News'])