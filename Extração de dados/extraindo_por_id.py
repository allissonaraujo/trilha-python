from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.infomoney.com.br')

driver.implicitly_wait(3)

dados1 = driver.find_element_by_id("high").text
dados2 = driver.find_elements_by_id("high")[0].text

print(dados1)
print("-------------")
print(dados2)
