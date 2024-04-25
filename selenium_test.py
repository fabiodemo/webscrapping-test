import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service


def downloads_running(dir):
    files = os.listdir(dir)
    return any(name for name in files if name.endswith('.crdownload'))


driver_path = 'msedgedriver.exe'
download_path = r'full-path\Downloads'

options = webdriver.EdgeOptions()
options.add_experimental_option('prefs', {
  "download.default_directory": download_path,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

s = Service(driver_path)
driver = webdriver.Edge(service=s, options=options)
driver.get('https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp')

WebDriverWait(driver, 1200).until(
    EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(), 'Acessar o recurso')]"))
)

buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Acessar o recurso')]")
print(buttons)

for button in buttons:
    driver.execute_script("arguments[0].click();", button)
    time.sleep(2)

while downloads_running(download_path):
    time.sleep(10)

driver.quit()
