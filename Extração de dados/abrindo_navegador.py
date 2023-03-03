#Import libs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Open link in browser
driver.get('https://www.infomoney.com.br')

#Implicitly wait of 3 seconds
driver.implicitly_wait(3)

