from selenium import webdriver
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
driver = webdriver. Chrome()

driver.maximize_window()

driver.get("https://www.magicbricks.com/")
driver.find_element(By.LINK_TEXT, "Sell").click()
time.sleep(5)
driver.quit()
