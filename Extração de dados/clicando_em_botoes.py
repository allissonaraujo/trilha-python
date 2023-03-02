#Import libs [Selenium]
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())

#Open link in browser
driver.get("http://imdb.com")

#Implicitly wait 4 seconds
driver.implicitly_wait(4)

#Find element with name "q"
busca = driver.find_element_by_name("q")
#Write in element "q" the word "Titanic"
busca.send_keys("Titanic")

#Implicitly wait 2 seconds
driver.implicitly_wait(2)

#Find element with id and click 
driver.find_element_by_id("suggestion-search-button").click()

#Sleep 5 seconds
time.sleep(5)

#Close the browser
driver.close()