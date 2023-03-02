from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.infomoney.com.br')

driver.implicitly_wait(3)

driver.minimize_window()

driver.implicitly_wait(3)

driver.maximize_window()

driver.implicitly_wait(5)

driver.get('https://www.uol.com.br')

driver.implicitly_wait(5)

driver.back()

driver.implicitly_wait(5)

driver.forward()

driver.implicitly_wait(5)

driver.refresh()

driver.implicitly_wait(5)

driver.close()


