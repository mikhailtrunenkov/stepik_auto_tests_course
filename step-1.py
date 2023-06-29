from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time 
import math

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome(executable_path="C:\\code\\chromedriver.exe")
    browser.get(link)
    
    # """ математическая функция """
    # def calc(x):
    #     return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.CSS_SELECTOR, "[id=input_value]")
    x = x_element.text
    y = calc(x)    
        
    # x_element  = x_element.get_attribute("valuex") возвращает значение в виде строки
    
    
    
    # num1 = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    # num2 = browser.find_element(By.CSS_SELECTOR, "[id='num2']")

    # num1_ = int(num1.text)
    # num2_ = int(num2.text)
    # y = num1_ + num2_
    
    # select = Select(browser.find_element(By.TAG_NAME, "select"))
    # select.select_by_value(f'{y}')

    # elements = browser.find_elements(By.TAG_NAME, "input")
    # for element in elements:
    #     element.send_keys("Мой ответ")


    # ex = str(math.ceil(math.pow(math.pi, math.e)*10000))
    # link = browser.find_element(By.PARTIAL_LINK_TEXT, f"{ex}")
    # link.click()
    
    # input1 = browser.find_element(By.TAG_NAME, 'input')
    input1 = browser.find_element(By.CLASS_NAME, 'form-control')
    input1.send_keys(y)
    
    
    # """ используем js-скрипт """
    # button = browser.find_element(By.TAG_NAME, "button")
    # l = browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    # input2 = browser.find_element(By.NAME, 'last_name')
    # input2 = browser.find_element(By.CLASS_NAME, 'form-control.second')
    # input2.send_keys("Petrov")
    # input3 = browser.find_element(By.CLASS_NAME, 'form-control.third')
    # input3.send_keys("Smolensk@ya.ru")
    input4 = browser.find_element(By.ID, "robotCheckbox")
    input4.click()
    input5 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    input5.click()
       
    
    
    # input4.send_keys("Russia")
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()
    # button = browser.find_element(By.XPATH, "//button[@type='submit']")
    # button.click()
    
    
    
finally:
    time.sleep(7)
    browser.quit()

# не забываем оставить пустую строку в конце файла