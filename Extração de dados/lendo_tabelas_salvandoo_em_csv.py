from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://www.clem.ufba.br/tuts/html/c09.htm")

driver.implicitly_wait(2)

driver.maximize_window()


dados = []
tabela = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/table[8]")

for linha in tabela.find_elements_by_tag_name("tr"):
    linhaDados = []
    for coluna in linha.find_elements_by_tag_name("td"):
        linhaDados.append(coluna.text)
        dados.append(linhaDados)

df = pd.DataFrame(dados)

df = df.iloc[1: , :]

df.columns = ["Tag HTML","O que faz?"]

print(df)

try:
    df.to_csv(r"C:\Users\allisson\Downloads\tabela.csv")
    print("CSV criado com sucesso!")
except:
    print("Ocorreu um erro ao criar o CSV!")

driver.quit()