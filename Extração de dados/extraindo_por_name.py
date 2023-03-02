from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://google.com")

driver.implicitly_wait(3)

search_box = driver.find_element_by_name("q")
search_box.send_keys("exemplo de pesquisa")

search_box.submit()

driver.implicitly_wait(10)
driver.quit()