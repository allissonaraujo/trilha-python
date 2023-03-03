#Import libs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Open link in browser
driver.get("http://uol.com.br")

#Implicitly Wait 2 seconds
driver.implicitly_wait(2)

#Find logo element
logo = driver.find_element_by_class_name("icon__image")
#Get Attribute SRC of logo
imagemLogo = logo.get_attribute("src")
#Print logo SRC
print("A imagem da LOGO :" + imagemLogo)
