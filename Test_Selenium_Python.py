import time 
from selenium.webdriver.common.by import By
import pytest 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get('https://suninjuly.github.io/cats.html')
browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]") # в кавычках текст взяли с сайта, где сами написали в строке find
bullet_cat = browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]")
print(bullet_cat.text)
#browser.quit()