#Import libs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open link in browser
driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

# Find elements by tag name and get the text inside of first element
nomeFii = driver.find_elements_by_tag_name("h1")[0].text

# Find elements by tag name and get the text inside of first element
valorAtual = driver.find_elements_by_tag_name("strong")[0].text

# Find elements by tag name and get the text inside of first element
tableaRendimentos = driver.find_elements_by_tag_name("table")[0].text

# Print all data extracted in screen and using the colorama lib for set colors in some words
print(Fore.RED + "Nome da FII:" + Style.RESET_ALL)
print(nomeFii)
print("----------------------------")
print(Fore.GREEN + "Valor atual" + Style.RESET_ALL) 
print(valorAtual)
print("----------------------------")
print(Fore.GREEN + "Tabela Rendimentos" + Style.RESET_ALL) 
print(tableaRendimentos)
print("-----------FINAL DO SCRAPPING-----------------")
