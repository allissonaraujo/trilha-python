from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://imdb.com/title/tt0120338/videogallery")

selectInput = Select(driver.find_element_by_name("sort"))

driver.implicitly_wait(3)

selectInput = Select(driver.find_element_by_name("sort"))
selectInput.select_by_visible_text("Duration")

driver.implicitly_wait(3)

Select(driver.find_element_by_name("sort")).select_by_index(0)

time.sleep(5)