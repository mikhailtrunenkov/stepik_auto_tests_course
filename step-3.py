from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import os
import time 
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome(executable_path="C:\\code\\chromedriver.exe")
    browser.get(link)
    
    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    """ математическая функция """
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.CSS_SELECTOR, "[id=input_value]")
    # x_element  = x_element.get_attribute("valuex")  возвращает значение в виде строки
    x = x_element.text
    y = calc(x)    
        
    input = browser.find_element(By.CLASS_NAME, 'form-control')
    input.send_keys(y)
    
    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()

finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла