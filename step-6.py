from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math

try:
    browser = webdriver.Chrome(executable_path="C:\\code\\chromedriver.exe")
    browser.implicitly_wait(5)
    
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    book_button = WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.ID, "book")))
    book_button.click()
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element(By.CLASS_NAME, 'form-control')
    input.send_keys(y)
    
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
        
finally:
    time.sleep(5)
    browser.quit()