#Import libs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Open link in browser
driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

#Implicitly wait 3 seconds
driver.implicitly_wait(3)

#Find one element by class name and get the text inside 
dados0 = driver.find_element_by_class_name("value").text

#Find elements by class name and get the text inside of first element 
dados1 = driver.find_elements_by_class_name("value")[0].text

#Find elements by class name and get the text inside of Thirdy element 
dados2 = driver.find_elements_by_class_name("value")[3].text

#Find elements by class name and get the text inside of Fourth element 
dados3 = driver.find_elements_by_class_name("value")[4].text

#Print in screen all dates extracted
print(dados0)
print(dados1)
print(dados2)
print(dados3)
