#Import libs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Browser
driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

# Implicitly wait 3 seconds
driver.implicitly_wait(3)

# Find elemenst for XPath and get the text inside that first element 
dataTabela = driver.find_elements_by_xpath("/html/body/main/div[2]/div[8]/div/div[7]/div/div[2]/table/tbody/tr[3]/td[2]")[0].text
# Find elemenst for XPath and get the text inside that first element 
numeroContratos = driver.find_elements_by_xpath("/html/body/main/div[2]/div[11]/div[2]/div[5]/div/div")[0].text

# Print all data extracted in scree
print("Data: ", dataTabela)
print("Número do contrato: ", numeroContratos)