from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
email = 'test16@superssqa.com'
password = 'Password123!'
url = 'http://demostore.supersqa.com/my-account/'
reg_btn = 'register'


# go to my account page:
myaccount = driver.get(url)

# input the email address
email_field = driver.find_element(By.ID,'reg_email').send_keys(email)

# input the password:
password_field = driver.find_element(By.ID,'reg_password').send_keys(password)

# click login button
reg_field = driver.find_element(By.NAME,reg_btn).click()
time.sleep(5)

# verify registration:

order_btn = driver.find_element(By.CSS_SELECTOR,'li.woocommerce-MyAccount-navigation-link--orders > a')

if order_btn.is_displayed():
    print('Registration successful')
assert Exception('Registration failed')



breakpoint()

