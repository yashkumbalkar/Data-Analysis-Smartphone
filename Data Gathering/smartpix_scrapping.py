from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

## code for  opening browser

from selenium.webdriver.chrome.options import Options
''' Defining driver path'''
s = Service("chromedriver.exe")

''' Set the different option for the browser'''
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])


''' Ignore the certificate and  SSL errors'''
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

''' Maximize the browser windows'''
chrome_options.add_argument('start-maximized')

''' Define the driver and open the browser'''
driver = webdriver.Chrome(service = s, options= chrome_options)


driver.get('https://www.smartprix.com/mobiles')
time.sleep(1)

driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/aside/div/div[5]/div[2]/label[2]/input').click()

time.sleep(2)

old_height = driver.execute_script('return document.body.scrollHeight')
while True:

    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source

with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)

