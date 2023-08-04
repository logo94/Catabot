from urllib.parse import urlsplit
import random
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime


def random_user():
    user_agents = [
    "Mozilla/5.0 (X11; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"
    "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
    ]
    random_user_agent = random.choice(user_agents)
    headers = {
        'User-Agent': random_user_agent,
        'lang': 'it-IT',
        'Connection': 'Close'
    }
    return headers

def get_host(url):
    host = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
    domain = urlsplit(host).netloc
    return host, domain

def get_html(url):
    page = requests.get(url, headers=random_user())
    if page.status_code != 200:
        raise Exception()
    soup = bs(page.text, 'html.parser')
    return soup

def check_url(url):
    page = requests.get(url, headers=random_user())
    if page.status_code != 200:
        raise Exception()

def normalize_url(host, href):
    # Normalizzazione URL
    if href == "" or href is None:
        raise Exception()
    if not 'http' in href:
        if './' in href:
            link = host + href.split('./')[1]
        elif href[0] == '/':
            link = host + href.replace('/', '', 1)
        else: raise Exception()
    else: link = href
    return link

def date():
    current_date = datetime.now()
    date_string = str(current_date.year) + str(current_date.month) + str(current_date.day) + str(current_date.hour) + str(current_date.minute) + str(current_date.second)
    return date_string

def headerow(coltype):
    if coltype == 'single':
        headerow = ['Identifier', 'Title', 'Creator', 'Publisher', 'Contributor', 'Date', 'Type', 'Format', 'Source', 'Language', 'Relation', 'Coverage', 'Rights', 'Description', 'Subject']
    elif coltype == 'multi':
        headerow = []
        headerow += 3*('Identifier',)
        headerow += 3*('Title',)
        headerow += 5*('Creator',)
        headerow += 3*('Publisher',)
        headerow += 3*('Contributor',)
        headerow += 3*('Date',)
        headerow += 3*('Type',)
        headerow += 3*('Format',)
        headerow += 3*('Source',)
        headerow += 3*('Language',)
        headerow += 3*('Relation',)
        headerow += 3*('Coverage',)
        headerow += 3*('Rights',)
        headerow += 3*('Description',)
        headerow += 9*('Subject',)
        headerow += ['Subject']
    return headerow

