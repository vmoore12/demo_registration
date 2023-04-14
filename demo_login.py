from selenium  import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
url = 'http://demostore.supersqa.com/my-account/'
log_user = 'username'
log_pass = 'password'
log_btn = 'button[value="Log in"]'

#go to web page:

logpage = driver.get(url)

# enter user name in username field:
user_field = driver.find_element(By.ID,log_user).send_keys('test15@superssqa.com')

#enter password in password field:
pass_field = driver.find_element(By.ID,log_pass).send_keys('Password123!')
time.sleep(5)

# click log in button:
login_button = driver.find_element(By.CSS_SELECTOR,log_btn).click()

breakpoint()

