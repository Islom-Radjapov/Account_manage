from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

# URL of website
url = "https://global.mytaurex.com/en/account-opening-process?fl=0"
login = "siwanac556@qodiq.com"
pasword = "Asd_1234"


# Here Chrome  will be used

driver = webdriver.Chrome()
driver.set_window_size(1550, 800)
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
    sleep(2)
except:
    pass
try:
    # waiting
    WebDriverWait(driver, 10)
    # Verifikatsiya oynasini olib tashlash uchun close knopkasini bosish
    driver.find_element(by=By.XPATH, value="//button[@type='button'][@class='close']").click()
    sleep(2)
except:
    pass
# waiting
WebDriverWait(driver, 10)
# pasroqga otkazish (mishka ortasidagini aylantirish)
driver.execute_script("window.scrollTo(0, 400)")
sleep(3)
# waiting
WebDriverWait(driver, 10)
# change knopkasini bosish
driver.find_element(by=By.XPATH, value="//button[@type='button'][@Class='btn btn-block btn-theme-secondary change-password']").click()
WebDriverWait(driver, 10)
sleep(3)
# eski parolni kiritish uchun bosish
driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control']").click()
driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control']").send_keys("Asdfg_123456")
WebDriverWait(driver, 10)
sleep(3)
# yangi parolni kiritish
driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control'][@name='password_new']").click()
driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control'][@name='password_new']").send_keys("SVkj2dvn12")
WebDriverWait(driver, 10)
sleep(3)
# yangi parolni tasdiqlash uchun kiritish
driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control'][@name='password_confirm']").click()
driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control'][@name='password_confirm']").send_keys("SVkj2dvn12")
# qoyilgan parolni o'zgartirish
driver.find_element(by=By.XPATH, value="//button[@id='passwordManageSaveVE'][@class='btn btn-theme-primary btn-tap-save']").click()
# waiting
WebDriverWait(driver, 10)
sleep(4)
driver.quit()
