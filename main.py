from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

PATH = "'C:/Program Files (x86)/chromedriver.exe"
USER = "cesar.rozas@avanzaprl.es"
PASSWORD = "PASSWORD"

def fichar():

    driver = webdriver.Chrome(PATH)
    driver.get('https://idalsoftware.es/login/')

    if driver.title == 'Login':
        email = driver.find_element(By.ID, "email")
        email.send_keys(USER)

        passwd = driver.find_element(By.ID, "password")
        passwd.send_keys(USER)

        driver.find_element(By.ID, "id_submit").click()

    time.sleep(5)

    if driver.title == 'Marcacíon':
        select = Select(driver.find_element(By.ID, 'id_estado'))
        select.select_by_visible_text('Entrada')

        driver.find_element(By.ID, "id_submit").click()


if __name__ == '__main__':
    fichar()

