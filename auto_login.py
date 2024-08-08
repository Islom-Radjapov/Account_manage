from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

def Change_password(email, pasword, old_password, new_password):
    driver = webdriver.Chrome()
    driver.set_window_size(1550, 800)
    driver.get("https://global.mytaurex.com/en/account-opening-process?fl=0")

    # waiting
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='userEmail'][@class='form-control userEmail']")))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='userPassword'][@class='form-control userPassword']")))
    # login kiritish
    driver.find_element(by=By.XPATH, value="//input[@id='userEmail'][@class='form-control userEmail']").click()
    driver.find_element(by=By.XPATH, value="//input[@id='userEmail'][@class='form-control userEmail']").send_keys(email)
    # parol kiritish
    driver.find_element(by=By.XPATH, value="//input[@id='userPassword'][@class='form-control userPassword']").click()
    driver.find_element(by=By.XPATH, value="//input[@id='userPassword'][@class='form-control userPassword']").send_keys(pasword)
    # login qib kirish knopkasini boish
    driver.find_element(by=By.XPATH, value="//button[@id='login_btn'][@class='btn btn-theme-primary btn-loader']").click()
    sleep(10)
    try:
        # waiting
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][@class='btn btn-default btn-close']")))
        # Get started oynasini olib tashlash uchun start knopkasini bosish
        driver.find_element(by=By.XPATH, value="//button[@type='button'][@class='btn btn-default btn-close']").click()
    except:
        pass
    try:
        # waiting
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][@class='close']")))
        # Verifikatsiya oynasini olib tashlash uchun close knopkasini bosish
        driver.find_element(by=By.XPATH, value="//button[@type='button'][@class='close']").click()
    except:
        pass
    # waiting
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][@class='close']")))
    # pasroqga otkazish (mishka ortasidagini aylantirish)
    driver.execute_script("window.scrollTo(0, 400)")
    # waiting
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][@Class='btn btn-block btn-theme-secondary change-password']")))
    # change knopkasini bosish
    driver.find_element(by=By.XPATH, value="//button[@type='button'][@Class='btn btn-block btn-theme-secondary change-password']").click()
    # waiting
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password'][@class='form-control']")))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password'][@class='form-control'][@name='password_new']")))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password'][@class='form-control'][@name='password_confirm']")))
    # eski parolni kiritish
    driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control']").click()
    driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control']").send_keys(old_password)
    # yangi parolni kiritish
    driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control'][@name='password_new']").click()
    driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control'][@name='password_new']").send_keys(new_password)
    # yangi parolni tasdiqlash
    driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control'][@name='password_confirm']").click()
    driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control'][@name='password_confirm']").send_keys(new_password)
    # qoyilgan parolni o'zgartirish
    driver.find_element(by=By.XPATH, value="//button[@id='passwordManageSaveVE'][@class='btn btn-theme-primary btn-tap-save']").click()
    # waiting
    sleep(5)
    driver.quit()
