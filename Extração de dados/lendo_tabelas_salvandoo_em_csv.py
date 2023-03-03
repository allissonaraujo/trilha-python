#Import libs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open link in browser
driver.get("http://www.clem.ufba.br/tuts/html/c09.htm")

# Implicitly wait 2 seconds
driver.implicitly_wait(2)

# Maximize windows of browser
driver.maximize_window()

#Open empty list
dados = []

# Find element by XPath (table)
tabela = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/table[8]")

# Loop for input the contents of rows and collumns in list elements and merge with append
for linha in tabela.find_elements_by_tag_name("tr"):
    linhaDados = []
    for coluna in linha.find_elements_by_tag_name("td"):
        linhaDados.append(coluna.text)
        dados.append(linhaDados)

# Create DataFrame with pandas with data extracted
df = pd.DataFrame(dados)

# Organizing rows and collumns
df = df.iloc[1: , :]

# Define names for Collumns
df.columns = ["Tag HTML","O que faz?"]

# Print DataFrame in Screen
print(df)

# Export datas for CSV archive with try and except for validate 
try:
    df.to_csv(r"C:\Users\allisson\Downloads\tabela.csv")
    print("CSV criado com sucesso!")
except:
    print("Ocorreu um erro ao criar o CSV!")

# Close browser
driver.quit()