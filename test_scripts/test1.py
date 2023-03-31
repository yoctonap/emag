from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.maximize_window()

driver.get('https://emag.ro')

# hover pe bacanie
bacanie = driver.find_element(By.XPATH, '//span[text()="Bacanie"]')
hover = ActionChains(driver).move_to_element(bacanie)
hover.perform()
sleep(2)

# click pe dulciuri
driver.find_element(By.XPATH, '//a[text()="Dulciuri"]').click()
sleep(2)

# adaugam in cos bomboane Merci rosu
# observati ca pornim de la nume produs
# urcam in sus prin div-uri pana avem adaugar in cos cuprinsa in div
# coboram in jos pana la butonul pe care scrie adauga in cos
driver.find_element(By.XPATH, '//a[contains(text(), "Biscuiti")]/parent::div/parent::div/parent::div//button[text()="Adauga in Cos"]').click()
sleep(2)
# asteptam sa se incarce vezi detalii cos - dureaza ceva pana apre popup
detalii_cos = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Vezi detalii cos")]')))

# click pe vezi detalii cos
detalii_cos.click()
sleep(2)
# click pe continua
driver.find_element(By.XPATH, '(//a[@href="/cart/checkout"])[1]').click()
sleep(2)
# verificam ca am ajuns pe pagina de login
assert driver.current_url == 'https://auth.emag.ro/user/login'

