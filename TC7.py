from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver. Chrome()
driver.maximize_window()
driver.get("https://www.magicbricks.com/")
driver.find_element(By.CSS_SELECTOR, ".mb-header__sub__tabs__link.js-menu-link.active").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Rates and Trends").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Pune")







#driver.quit()
