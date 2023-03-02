from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://imdb.com/title/tt0120338/mediaindex?ref=tt_pv_mi_sm")

driver.implicitly_wait(3)

divImagens = driver.find_element_by_id("media_index_thumbnail_grid")
primeiraImagem = divImagens.find_elements_by_tag_name("img")[1]
atributoSrc = primeiraImagem.get_attribute("src")
print(atributoSrc)

try:
    urllib.request.urlretrieve(atributoSrc, r"C:\Users\allisson\Downloads\imagem.jpg")
    print("Imagem baixada com sucesso!")
except:
    print("Ocorreu um erro ao tentar baixar a imagem!")