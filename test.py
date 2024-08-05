from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# URL of website
url = "https://global.mytaurex.com/en/account-opening-process?fl=0"
login = "siwanac556@qodiq.com"
pasword = "Asd_1234"


# Here Chrome  will be used

driver = webdriver.Chrome()
#driver.set_window_size(800, 600)
driver.get(url)

# waiting
WebDriverWait(driver, 10)

# login kiritish
driver.find_element(by=By.XPATH, value="//input[@id='userEmail'][@class='form-control userEmail']").click()
driver.find_element(by=By.XPATH, value="//input[@id='userEmail'][@class='form-control userEmail']").send_keys(login)
# parol kiritish
driver.find_element(by=By.XPATH, value="//input[@id='userPassword'][@class='form-control userPassword']").click()
driver.find_element(by=By.XPATH, value="//input[@id='userPassword'][@class='form-control userPassword']").send_keys(pasword)
# login qib kirish knopkasini boish
driver.find_element(by=By.XPATH, value="//button[@id='login_btn'][@class='btn btn-theme-primary btn-loader']").click()
sleep(20)
try:
    # waiting
    WebDriverWait(driver, 10)
    # Get started oynasini olib tashlash uchun start knopkasini bosish
    driver.find_element(by=By.XPATH, value="//button[@type='button'][@class='btn btn-default btn-close']").click()
    sleep(4)
except:
    pass
try:
    # waiting
    WebDriverWait(driver, 10)
    # Verifikatsiya oynasini olib tashlash uchun close knopkasini bosish
    driver.find_element(by=By.XPATH, value="//button[@type='button'][@class='btn btn-theme-secondary']").click()
    sleep(4)
except:
    pass
# parolni ochish uchun ko'z knopkasini bosish
driver.find_element(by=By.CLASS_NAME, value="input-group-addon ma-toggle-password").click()
# change knopkasini bosish



# waiting
WebDriverWait(driver, 10)


sleep(10)
#driver.refresh()