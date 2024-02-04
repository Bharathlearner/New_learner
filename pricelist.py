from selenium import webdriver
import openpyxl
import os
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r'C:\Users\Golla Bharath\Downloads\chromedriver_win32\chromedriver.exe')  # You may need to download the ChromeDriver executable and provide its path here
print(driver)
driver.maximize_window()
url = 'https://www.globalpetrolprices.com/countries/'  # Replace with the actual website URL
driver.get(url)
gasoline_prices = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[3]/a').click()
sleep(10)
# Assuming the data is in a table with rows and columns
table_rows = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[3]/a')

data = []  # To store the extracted data




date = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[3]/span')
date = date.text
date = date.split()
# #print(options)
# date = date.text
# date = date.split()
print(date)
#os.remove('data.xlsx')
wb = openpyxl.Workbook()
sheet = wb.active

headers = ['S.NO', 'Country', 'Currency', 'Date', 'Gas_prices', 'Diesel_prices', 'LPG_prices', 'Kerosene_prices']
sheet.append(headers)

driver.find_element(By.ID, 'highlightCountry').click()
dropdown = Select(driver.find_element(By.ID, 'highlightCountry'))
country_list_count = str(len(dropdown.options))
country_list = int(country_list_count)
driver.find_element(By.ID, 'highlightCountry').click()

data = []  # To store the extracted data

# ... Rest of the code ...

for i in range(country_list - 1):
    country_name = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[4]/div/div[{0}+1]/a'.format(i))
    if '*' in country_name.text:
        country_name1 = country_name.text
        country_name2 = country_name1.split('*')
        country_name = country_name2[0]
    else:
        country_name = country_name.text
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[4]/div/div[{0}+1]/a'.format(i)).click()
    sleep(10)
    country_currency_name = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/table/tbody/tr[1]/th')
    gasoline_price = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/table/tbody/tr[1]/td[1]')
    usd_currency_name = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/table/tbody/tr[2]/th')
    gasoline_price_usd = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/table/tbody/tr[2]/td[1]')


    #print(country_name)
    # default_currency = 'USD'
    # driver.find_element(By.ID, 'currency').click()
    # currency = Select(driver.find_element(By.ID, 'currency'))
    # currency.select_by_value(default_currency)
    # gasoline_price_USD = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[5]/div/div[{0}+3]/div'.format(i))
    # driver.find_element(By.ID, 'currency').click()
    # currency = Select(driver.find_element(By.ID, 'currency'))
    # for j in currency.options:
    #     name = j.get_attribute('value')
    #     currency_name = j.get_attribute('innerHTML')
    #     #print(name, currency_name, country_name)
    #     if name != '' and country_name in currency_name:
    #         currency.select_by_value(name)
    #         sleep(3)
    #         break
    #     else:
    #         continue
    # gasoline_price = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[1]/div[5]/div/div[{0}+3]/div'.format(i))

    data.append([i+1, country_name, country_currency_name.text, date[2], gasoline_price.text],)
    data.append([i+1, country_name, country_currency_name.text + '_' + usd_currency_name.text, date[2], gasoline_price_usd.text],)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[3]/a').click()

# Save the data to Excel
for row_data in data:
    sheet.append(row_data)

file_name = 'data.xlsx'  # Provide a file name for the Excel file
wb.save(file_name)

