from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

csvFile = open('test.csv', 'w+')
html = urlopen('https://bank.gov.ua/markets/exchangerates/?date=21.03.2020&period=daily')
bs = BeautifulSoup(html.read(), 'html.parser')
curensis = bs.find(id='exchangeRates').tbody

try:
    writer = csv.writer(csvFile)
    writer.writerow(curensis.get_text())
finally:
    csvFile.close()
