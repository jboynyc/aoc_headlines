import datetime
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


def _memeorandum_clusters(date, time):
    'Get clusters of Memeorandum news stories for a date.'
    _url = 'https://www.memeorandum.com/{}/h{}'
    if isinstance(date, str):
        try:
            date = datetime.date(*map(int, date.split('-')))
        except:
            raise ValueError('Invalid date', date)
    lnk = _url.format(date.strftime('%y%m%d'), time)
    r = requests.get(lnk)
    r.raise_for_status()
    s = bs(r.text, 'lxml')
    return s.find('div', {'class': 'nornbody'}).findAll('div', {'class': 'clus'})


def _cluster_lead_data(clus):
    'Get data for the lead story in a cluster.'
    lead_headline = clus.find('div', {'class': 'ii'}).find('strong').text
    lead_link = clus.find('div', {'class': 'ii'}).find('strong').find('a')['href']
    lead_author = clus.find('cite').text.split('/')[0].strip().strip(':')
    lead_pub = clus.find('cite').find('a').text
    return lead_author, lead_pub, lead_headline, lead_link


def lead_stories(date, time='1200'):
    'Generate a data frame of lead news stories for specified date and time (default is noon EST).'
    data = map(_cluster_lead_data, _memeorandum_clusters(date, time))
    df = pd.DataFrame(list(data), columns=['author', 'publication', 'headline', 'url'])
    df = df.reset_index().rename(columns={'index': 'rank'})
    df['rank'] = df['rank'] + 1
    df['date'] = date
    return df
