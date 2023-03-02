from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

driver.implicitly_wait(3)

dataTabela = driver.find_elements_by_xpath("/html/body/main/div[2]/div[8]/div/div[7]/div/div[2]/table/tbody/tr[3]/td[2]")[0].text
numeroContratos = driver.find_elements_by_xpath("/html/body/main/div[2]/div[11]/div[2]/div[5]/div/div")[0].text

print("Data: ", dataTabela)
print("Número do contrato: ", numeroContratos)