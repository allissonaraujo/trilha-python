#Import libs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open link in browser
driver.get("https://imdb.com/title/tt0120338/videogallery")

# Manipulating select element with find element by name 
selectInput = Select(driver.find_element_by_name("sort"))

# Implicitly wait 3 seconds
driver.implicitly_wait(3)

# Manipulating select element with find element by name 
selectInput = Select(driver.find_element_by_name("sort"))
# Change the select element value
selectInput.select_by_visible_text("Duration")

# Implicitly wait 3 seconds
driver.implicitly_wait(3)

# Manipulating select element with find element by index 
Select(driver.find_element_by_name("sort")).select_by_index(0)

# Sleep 5 seconds
time.sleep(5)