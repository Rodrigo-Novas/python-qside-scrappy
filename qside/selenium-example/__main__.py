from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import fitz
# Uso este comando para poder importar el binario y los paquetes que estan en el venv
# pyinstaller --paths venv/lib/python3.7/site-packages -F --add-binary "C:\Users\novasrodrigo\Desktop\qside\selenium-example\chromedriver.exe";"." __main__.py
driver = webdriver.Chrome(r"C:\Users\novasrodrigo\Desktop\qside\selenium-example\chromedriver.exe")
driver.get("http://www.google.com")


def buscador():
    try:
        buscador = driver.find_element_by_name("q")
        buscador.clear()
        buscador.send_keys("gatitos")
        buscador.send_keys(keys.Keys.ENTER)
        imagenes = driver.find_element_by_xpath("//*[@id='hdtb-msb']/div[1]/div/div[2]/a")
        imagenes.click()
        print("espera")

    except NoSuchElementException as e:
        print(f"No se encuentra el elemento: {e}")

def pdf_html():
    doc = fitz.open(r"C:\Users\novasrodrigo\Desktop\qside\selenium-example\Hostinger Empresas-Julio-2021_HomeDays (2).jpg.pdf") 
    for page in doc:
        text = page.get_text("html")
    with open("pdf_txt.html", "w") as f:
        f.write(text)
if __name__ == "__main__":
    buscador()
    pdf_html()
