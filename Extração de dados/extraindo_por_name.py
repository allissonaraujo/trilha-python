#Import libs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open link in browser
driver.get("https://google.com")

# Implicitly wait 3 seconds
driver.implicitly_wait(3)

# Find one element by name "q"
search_box = driver.find_element_by_name("q")

# Write (type) in element 
search_box.send_keys("exemplo de pesquisa")
# Submit method on form that element
search_box.submit()

# Implicitly wait 10 seconds
driver.implicitly_wait(10)

# Quit (close) browser
driver.quit()