from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Directorio donde debemos dejar el driver
PATH = "C:\Program Files (x86)\chromedriver.exe"

# Usuario de la aplicacion
USER = "*"

# Contrasenya del usuario
PASSWORD = "*"

def fichar():

    # Accedemos a la pagina
    driver = webdriver.Chrome(PATH)
    driver.get('https://idalsoftware.es/login/')

    # Si se acuerda del login no haremos nada
    if driver.title == 'Login':
        # Accedemos con nuestro usuario
        email = driver.find_element(By.ID, "email")
        email.send_keys(USER)

        passwd = driver.find_element(By.ID, "password")
        passwd.send_keys(PASSWORD)

        driver.find_element(By.ID, "id_submit").click()

        time.sleep(2)

    # Marcamos la entrada
    if driver.title == 'Marcación':
        select = Select(driver.find_element(By.ID, 'id_estado'))
        select.select_by_visible_text('Salida')

        driver.find_element(By.ID, "id_submit").click()
        time.sleep(2)
    # Cerramos el navegador
    driver.quit()

if __name__ == '__main__':
    fichar()