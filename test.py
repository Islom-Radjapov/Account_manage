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
sleep(10)
try:
    # waiting
    WebDriverWait(driver, 10)
    # Get started oynasini olib tashlash uchun start knopkasini bosish
    driver.find_element(by=By.XPATH, value="//button[@type='button'][@class='btn btn-default btn-close']").click()
    #sleep(4)
except:
    pass
try:
    # waiting
    WebDriverWait(driver, 10)
    # Verifikatsiya oynasini olib tashlash uchun close knopkasini bosish
    driver.find_element(by=By.XPATH, value="//button[@type='button'][@class='btn btn-theme-secondary']").click()
    sleep(2)
except:
    pass
# waiting
WebDriverWait(driver, 10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#WebDriverWait.execute_script("window.scrollBy(0,40)")
WebDriverWait(driver, 10)
# change knopkasini bosish
a = driver.find_element(by=By.XPATH, value="//button[@type='button'][@data-trade_platform_id='710004333'][@data-account_id='29890']").click()
# eski parolni kiritish uchun bosish
#driver.find_element(by=By.XPATH, value="//input[@id='password'][@class='form-control']").send_keys("Asdfg_123456")

print(a)

# waiting
WebDriverWait(driver, 10)


sleep(10)
#driver.refresh()