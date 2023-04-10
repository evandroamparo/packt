from bs4 import BeautifulSoup
import requests

url = 'https://www.packtpub.com/free-learning'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

book = soup.find('div', class_='grid product-info main-product')

title = book.find('h3', class_='product-info__title').text
author = book.find('span', class_='product-info__author free_learning__author').text
author = author.split("By")
author = "".join(author).strip()
publication_date = book.find('div', class_='free_learning__product_pages_date').find('span').text
pages = book.find('div', class_='free_learning__product_pages').find('span').text
description = book.find('div', class_='free_learning__product_description').find('span').text
image_url = book.find('img', class_='product-image')['src']

print('Title:', title)
print('Author:', author)
print('Publication date:', publication_date)
print('Pages:', pages)
print('Description:', description)
print('Image URL:', image_url)
