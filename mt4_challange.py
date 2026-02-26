import random
import string
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import psutil

# Close MetaTrader using the process name
def close_MT4():
    for proc in psutil.process_iter():
        try:
            print(proc)
            # Check if process name matches MetaTrader
            if proc.name() == "terminal.exe":  # This is the name for both MT4 and MT5
                proc.terminate()  # or proc.kill() for a forced termination
                print("MetaTrader closed successfully.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


def Change_password(email, pasword, old_password, new_password):
    try:
        driver = webdriver.Edge()
        #driver.set_window_size(1550, 800)
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
        # pasroqga otkazish (mishka ortasidagini aylantirish)
        driver.execute_script("window.scrollTo(0, 400)")
        # waiting
        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.CLASS_NAME, "modal-backdrop")))
        # change knopkasini bosish
        btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][@Class='btn btn-block btn-theme-secondary change-password']")))
        btn.click()
        # change knopkasini bosish id orqali iminoy tanlab bosish
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-trade_platform_id='810004304' and @data-account_id='33900' and @data-at-id='3']"))).click()
        # waiting
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password'][@class='form-control']")))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password'][@class='form-control'][@name='password_new']")))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password'][@class='form-control'][@name='password_confirm']")))
        # eski parolni kiritish
        driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control']").click()
        driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control']").send_keys(old_password)
        # yangi parolni kiritishi ined
        driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control'][@name='password_new']").click()
        driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control'][@name='password_new']").send_keys(new_password)
        # yangi parolni tasdiqlash
        driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control'][@name='password_confirm']").click()
        driver.find_element(by=By.XPATH, value="//input[@type='password'][@class='form-control'][@name='password_confirm']").send_keys(new_password)
        # qoyilgan parolni o'zgartirish
        driver.find_element(by=By.XPATH, value="//button[@id='passwordManageSaveVE'][@class='btn btn-theme-primary btn-tap-save']").click()

        # waiting
        sleep(10)
        driver.quit()
    except Exception as error:
        try:
            print("ERROR try => ", error)
            driver.quit()
        except:
            pass


def generate_password(length=8):

    # Define character sets based on the requirements
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_characters = "!@$%_#()"

    # Ensure the password contains at least one character from each required set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(numbers),
        random.choice(special_characters)
    ]

    # Fill the remaining length with random choices from allowed characters
    allowed_characters = lowercase_letters + uppercase_letters + numbers + special_characters
    password += random.choices(allowed_characters, k=length - 4)
    # Shuffle to ensure random order and join to create the password string
    random.shuffle(password)
    return ''.join(password)


email = "*"
pasword = "*"
old_password = "*"
new_password = generate_password(13)


print("Start checking")

while True:
    try:
        with open(r"C:\Users\Administrator\AppData\Roaming\MetaQuotes\Terminal\2191F4A3D14D7B4B1EBB84F924777883\MQL4\Files\loss.csv", encoding='utf-16') as file:
            print("file open > ", file.read())
            print("bool > ", file.read() is not None)
            if file is not None:
                print("Change password active")
                close_MT4()
                Change_password(email, pasword, old_password, new_password)
    except:
        pass
    sleep(15)
