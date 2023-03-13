import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
vars = {}
driver.get("https://www.magicbricks.com/")
driver.maximize_window()
driver.delete_all_cookies()
driver.find_element(By.LINK_TEXT, 'Sell').click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Ad Packages").click()
time.sleep(5)
child_window_handle = driver.window_handles[-1]
driver.switch_to.window(child_window_handle)
driver.find_element(By.CSS_SELECTOR, "#userTypeList > .active > label").click()
driver.find_element(By.CSS_SELECTOR, "#sellId > label").click()
driver.find_element(By.CSS_SELECTOR, ".m-t-10:nth-child(4) .active > label").click()
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(4)
driver.find_element(By.LINK_TEXT, "Buy Now").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Add to My Orders").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".orderNoArrow").click()

driver.quit()