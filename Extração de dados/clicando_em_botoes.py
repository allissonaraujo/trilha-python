from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://imdb.com")

driver.implicitly_wait(4)

busca = driver.find_element_by_name("q")
busca.send_keys("Titanic")

driver.implicitly_wait(2)

driver.find_element_by_id("suggestion-search-button").click()

time.sleep(5)