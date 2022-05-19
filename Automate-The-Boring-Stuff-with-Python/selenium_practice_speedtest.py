

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
browser.get('https://www.speedtest.net/')

linkElem = browser.find_element(By.CLASS_NAME, 'start-text')

type(linkElem)

linkElem.click()
