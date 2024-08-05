from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
url1 = "https://kortanafx.com/"
# URL of website
url = "https://global.mytaurex.com/en/account-opening-process?fl=0"
login = "siwanac556@qodiq.com"
pasword = "Asd_1234"


# Here Chrome  will be used

driver = webdriver.Chrome()
#driver.set_window_size(800, 600)
driver.get(url)

driver.implicitly_wait(10)
#WebDriverWait(driver, 10).until(EC.find_element_by_id(By.XPATH, "//input[@id='userEmail']"))

#username = driver.find_element_by_name("userEmail")#.send_keys(login))
driver.find_element(by=By.XPATH, value="//input[@id='userEmail'][@class='form-control userEmail']").click()
driver.find_element(by=By.XPATH, value="//input[@id='userEmail'][@class='form-control userEmail']").send_keys(login)

driver.find_element(by=By.XPATH, value="//input[@id='userPassword'][@class='form-control userPassword']").click()
driver.find_element(by=By.XPATH, value="//input[@id='userPassword'][@class='form-control userPassword']").send_keys(pasword)


#username = driver.find_element(by=By.CLASS_NAME, value="btn btn-primary")
#print(username)
#a = driver.find_element(by=By.CLASS_NAME, value="btn btn-primary")


sleep(3)
# getting the button by class name
#button = driver.find_element(by='id', value=id)

# clicking on the button
#button.click()



