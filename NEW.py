from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'C:\Users\Golla Bharath\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://atwork.atai.ai/login")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("Bharath.golla@soctronics.com")
password.send_keys("Soct@1234")
password.send_keys(Keys.RETURN)

# You can also directly locate the login button by its text
login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
login_button.click()

# Add appropriate wait statements if necessary
