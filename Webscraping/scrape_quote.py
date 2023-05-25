#Brian Reyna Castillo 2127309
import requests
import csv
from bs4 import BeautifulSoup
url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
quotes_html = html.find_all('span', class_="text")
authors_html = html.find_all('small', class_="author")
quotes = list()
for quotes in quotes_html:
    quotes.append(quotes.text)
authors = list()
for authors in authors_html:
    authors.append(authors.text)
for t in zip(quotes, authors):
    print(t)
with open("./citas_2127309.csv", 'w') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes, authors))
    
