from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = 'msedgedriver.exe'

driver = webdriver.Edge(executable_path=driver_path)

driver.get('https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp')


wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.ID, 'btnDownloadUrl')))

button.click()

time.sleep(5)

download_link = driver.find_element(By.CLASS_NAME, 'download-link')

file_url = download_link.get_attribute('href')

driver.quit()
