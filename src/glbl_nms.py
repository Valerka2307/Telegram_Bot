import requests
from bs4 import BeautifulSoup


dictionary = {}
names = []


dictionary_next = {}
currency = []
currency_1 = []


URL = 'https://bitinfocharts.com/ru/crypto-kurs/'
cripta = requests.get(URL)
soup = BeautifulSoup(cripta.text, 'lxml')

BLOCKS = soup.findAll('tr', {'class' : 'ptr'}, limit=10)

TOKEN = '5773512698:AAGJ-O5vrMdQ_7Mbz-qDbdhMjKHwSXAULT4'
