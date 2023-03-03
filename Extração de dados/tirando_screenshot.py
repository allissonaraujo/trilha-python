#Import libs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://inboxagenciadigital.com.br"
driver.get(url)

driver.maximize_window()

try:
    driver.get_screenshot_as_file(r"C:\Users\allisson\Downloads\Prints Websites\teste.png")
    print("Screenshot da url:" + url + " tirado com sucesso!" )
except:
    print("Ouve um erro ao tirar o print!")
    
    
driver.close()