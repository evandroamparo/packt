from bs4 import BeautifulSoup
import requests

url = 'https://www.packtpub.com/free-learning'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

livro = soup.find('div', class_='grid product-info main-product')

titulo = livro.find('h3', class_='product-info__title').text
autor = livro.find('span', class_='product-info__author free_learning__author').text
autor = autor.split("By")
autor = "".join(autor).strip()
data_publicacao = livro.find('div', class_='free_learning__product_pages_date').find('span').text
numero_paginas = livro.find('div', class_='free_learning__product_pages').find('span').text
descricao = livro.find('div', class_='free_learning__product_description').find('span').text
imagem_url = livro.find('img', class_='product-image')['src']

print('Título:', titulo)
print('Autor:', autor)
print('Data de publicação:', data_publicacao)
print('Número de páginas:', numero_paginas)
print('Descrição:', descricao)
print('URL da imagem:', imagem_url)
