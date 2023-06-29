from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import os
import time 
import math

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome(executable_path="C:\\code\\chromedriver.exe")
    browser.get(link)
    
    first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    first_name.send_keys("Petr")
    
    second_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    second_name.send_keys("Petrov")
    
    mail = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    mail.send_keys("petrov@gmail.com")   
    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file_text = browser.find_element(By.ID, 'file')
    file_text.send_keys(file_path)
    
    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()

finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла