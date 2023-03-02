from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://uol.com.br")

driver.implicitly_wait(2)

logo = driver.find_element_by_class_name("icon__image")
imagemLogo = logo.get_attribute("src")
print("A imagem da LOGO :" + imagemLogo)
