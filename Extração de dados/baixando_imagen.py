#Imports libs[Selenium]
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
driver = webdriver.Chrome(ChromeDriverManager().install())

#Open link in browser
driver.get("https://imdb.com/title/tt0120338/mediaindex?ref=tt_pv_mi_sm")

#Implicitly wait of 3 seconds
driver.implicitly_wait(3)

#Find DIV with ghumbnail images
divImagens = driver.find_element_by_id("media_index_thumbnail_grid")

#Get First Image 
primeiraImagem = divImagens.find_elements_by_tag_name("img")[1]
#Get Attribute SRC
atributoSrc = primeiraImagem.get_attribute("src")
#Prin in screen the attribute
print(atributoSrc)

#Make download with urllib request with verification with try and except
try:
    urllib.request.urlretrieve(atributoSrc, r"C:\Users\allisson\Downloads\imagem.jpg")
    print("Imagem baixada com sucesso!")
except:
    print("Ocorreu um erro ao tentar baixar a imagem!")