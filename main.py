from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import time


# Directorio donde debemos dejar el driver
PATH = "C:\Program Files (x86)\chromedriver.exe"

# Usuario de la aplicacion
USER = "*"

# Contrasenya del usuario
PASSWORD = "*"

WORKIN_SPACE = 'equipo-otp'

EMOJIS = ['( •̀ ω •́ )y', '(づ￣ 3￣)づ', '~\(≧▽≦)/~', '(★ ω ★)', '☆*: .｡. o(≧▽≦)o .｡.:*☆']

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
        select.select_by_visible_text('Entrada')

        driver.find_element(By.ID, "id_submit").click()
        time.sleep(2)
    # Cerramos el navegador
    driver.quit()


def saludar():

    now = datetime.today().weekday()

    # Accedemos a la pagina
    driver = webdriver.Chrome(PATH)
    driver.get('https://slack.com/workspace-signin')

    email = driver.find_element(By.ID, "domain")
    email.send_keys(WORKIN_SPACE)

    driver.find_element_by_xpath('//*[@id="page_contents"]/div/div/div[1]/div[2]/form/button').click()
    time.sleep(2)

    email = driver.find_element(By.ID, "email")
    email.send_keys(USER)

    passwd = driver.find_element(By.ID, "password")
    passwd.send_keys(PASSWORD)

    driver.find_element(By.ID, "signin_btn").click()
    time.sleep(2)

    # try:
    #     element = WebDriverWait(driver, 15).until(
    #         EC.visibility_of_element_located((By.XPATH, '//*[@id="page_contents"]/div/div/div[2]/p/a'))
    #     )
    # except Exception as e:
    #     print(e)

    driver.get('https://app.slack.com/client/T836R8Q57/GU5M108BH')
    time.sleep(6)

    driver.execute_script("document.querySelector('.ql-editor p').innerHTML = 'Buenos dias "+EMOJIS[now]+"';")
    time.sleep(1)

    driver.execute_script("document.querySelector('.c-wysiwyg_container__button--send').click();")
    time.sleep(1)

    driver.execute_script("document.querySelector('.ql-editor p').innerHTML = '/giphy good morning';")
    time.sleep(1)

    driver.execute_script("document.querySelector('.c-wysiwyg_container__button--send').click();")
    time.sleep(3)

    driver.execute_script("document.getElementById('post-giphy:ephemeral_preview').click();")
    time.sleep(2)

    # Cerramos el navegador
    driver.quit()


if __name__ == '__main__':

    resultado = input('¿Desea fichar la entrada? [y/other key]')
    resultado_fichar = input('¿Desea saludar? [y/other key]')

    if resultado.upper() == 'Y':
        fichar()

    if resultado_fichar.upper() == 'Y':
        saludar()
