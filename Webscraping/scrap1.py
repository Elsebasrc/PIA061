#Brian Reyna Castillo 2127309
import requests
URL= "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
print(page.text)