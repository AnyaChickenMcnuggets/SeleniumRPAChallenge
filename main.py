import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

data = pd.read_excel('data_read/challenge.xlsx')

fields = ['labelFirstName', 'labelLastName', 'labelCompanyName', 'labelRole', 'labelAddress',
          'labelEmail', 'labelPhone']
data.columns = fields

driver = webdriver.Chrome()
driver.get('https://www.rpachallenge.com/')

driver.find_element(By.XPATH, "//button[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']")\
    .send_keys(Keys.RETURN)

for i in range(len(data)):
    for j in range(len(fields)):
        driver.find_element(By.XPATH, f"//input[@ng-reflect-name='{fields[j]}']")\
            .send_keys(str(data[fields[j]][i]))
    driver.find_element(By.XPATH, "//input[@type='submit']").send_keys(Keys.RETURN)

time.sleep(10)
