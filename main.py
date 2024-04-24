import requests
from bs4 import BeautifulSoup

url = 'page'

response = requests.get(url)
response.raise_for_status()  # isso vai lançar uma exceção se a requisição falhar

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a', text='acessar recurso')

# Iterar sobre cada link encontrado e fazer o download do CSV
for link in links:
    href = link.get('href')
    if href:
        download_response = requests.get(href)
        download_response.raise_for_status()  # isso vai lançar uma exceção se a requisição falhar
        
        filename = href.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(download_response.content)
        print(f'Arquivo {filename} baixado com sucesso.')
