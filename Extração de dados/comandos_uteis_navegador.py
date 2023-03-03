#Import libs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Open link in browser
driver.get('https://www.infomoney.com.br')

#Implicitly wait 3 seconds
driver.implicitly_wait(3)

#Minimize windows of borwser
driver.minimize_window()

#Implicitly wait 3 seconds
driver.implicitly_wait(3)

#Maximize windows of browser
driver.maximize_window()

#Implicitly wait 5 seconds
driver.implicitly_wait(5)

#Open link in browser
driver.get('https://www.uol.com.br')

#Implicitly wait 5 seconds
driver.implicitly_wait(5)

#Back page in browser
driver.back()

#Implicitly wait 5 seconds
driver.implicitly_wait(5)

#Forward page
driver.forward()

#Implicitly wait 5 seconds
driver.implicitly_wait(5)

#Refresh page
driver.refresh()

#Implicitly wait 5 seconds
driver.implicitly_wait(5)

#Close Borwser
driver.close()


