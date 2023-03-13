import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
vars = {}

driver.maximize_window()
driver.get("https://www.magicbricks.com/")

driver.find_element(By.LINK_TEXT, "Sell").click()
time.sleep(3)

#driver.get("https://www.magicbricks.com/bricks/packageGroup.html?Package=50883")
driver.find_element(By.LINK_TEXT,"iAdvantage").click()
time.sleep(5)
child_window_handle = driver.window_handles[-1]
driver.switch_to.window(child_window_handle)
#driver.set_window_size(1296, 688)
driver.find_element(By.LINK_TEXT, "Add to My Orders").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".orderNoArrow").click()
driver.quit()