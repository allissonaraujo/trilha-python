from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from colorama import  Fore, Style

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

nomeFii = driver.find_elements_by_tag_name("h1")[0].text

valorAtual = driver.find_elements_by_tag_name("strong")[0].text

tableaRendimentos = driver.find_elements_by_tag_name("table")[0].text


print(Fore.RED + "Nome da FII:" + Style.RESET_ALL)
print(nomeFii)
print("----------------------------")
print(Fore.GREEN + "Valor atual" + Style.RESET_ALL) 
print(valorAtual)
print("----------------------------")
print(Fore.GREEN + "Tabela Rendimentos" + Style.RESET_ALL) 
print(tableaRendimentos)
print("-----------FINAL DO SCRAPPING-----------------")
