import requests
from bs4 import BeautifulSoup

url = "https://www.mathieu-crevoulin.com/"
page = requests.get(url) # récupère le code HTML du site

# Récupérer le code HTML source
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.head)
print(soup.title)
print(soup.title.string)

soup.find_all('link')
boxes =  soup.find_all('div', class_="box")

for box in boxes:
    print(box)

boxClasses = []
for box in boxes:
    boxClasses.append(box.string)

