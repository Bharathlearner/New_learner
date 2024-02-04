from selenium import webdriver
import openpyxl
import os
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Setting up WebDriver
driver = webdriver.Chrome(executable_path=r'C:\Users\Golla Bharath\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window()

# Accessing the website
url = 'https://www.globalpetrolprices.com/countries/'
driver.get(url)
sleep(10)

# Clicking on gasoline prices
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[3]/a').click()
sleep(10)

# Extracting data
date = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[3]/span').text.split()
os.remove('data.xlsx')
wb = openpyxl.Workbook()
sheet = wb.active
headers = ['S.NO', 'Country', 'Currency', 'Date', 'Gas_prices', 'Diesel_prices', 'LPG_prices', 'Kerosene_prices']
sheet.append(headers)

# Extracting data for each country
dropdown = Select(driver.find_element(By.ID, 'highlightCountry'))
country_list = len(dropdown.options)

data = []
for i in range(country_list - 1):
    country_name_element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[4]/div/div[{0}+1]/a'.format(i))
    country_name = country_name_element.text.split('*')[0] if '*' in country_name_element.text else country_name_element.text
    country_name_element.click()
    sleep(10)
    country_currency_name = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/table/tbody/tr[1]/th').text
    gasoline_price = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/table/tbody/tr[1]/td[1]').text
    usd_currency_name = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/table/tbody/tr[2]/th').text
    gasoline_price_usd = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/table/tbody/tr[2]/td[1]').text

    data.append([i+1, country_name, country_currency_name, date[2], gasoline_price])
    data.append([i+1, country_name, country_currency_name + '_' + usd_currency_name, date[2], gasoline_price_usd])
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[3]/a').click()

# Save the data to Excel
for row_data in data:
    sheet.append(row_data)

file_name = 'data.xlsx'
wb.save(file_name)
