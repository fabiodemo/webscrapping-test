"""<button data-v-55a04e1a="" id="btnDownloadUrl" type="button" class="btn btn btn-secondary btn-secondary"> Acessar o recurso </button>
The element is a button and not a href, so we need another tool to download all CSVs.
"""

import requests
from bs4 import BeautifulSoup

url = 'https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a', string='Acessar o recurso')

for link in links:
    href = link.get('href')
    if href:
        download_response = requests.get(href)
        download_response.raise_for_status()
        
        filename = href.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(download_response.content)
        print(f'File {filename} downloaded.')
