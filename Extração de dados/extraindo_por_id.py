#Import libs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Open link in browser
driver.get('https://www.infomoney.com.br')

# Implicitly wait 3 seconds
driver.implicitly_wait(3)

# Find one element by id and get inside text
dados1 = driver.find_element_by_id("high").text

# Find one elements by id and get inside text of First Element 
dados2 = driver.find_elements_by_id("high")[0].text

# Print in screen all data extracted
print(dados1)
print(dados2)
