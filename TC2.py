from selenium import webdriver
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
driver = webdriver. Chrome()

driver.maximize_window()

driver.get("https://www.magicbricks.com/")

driver.find_element(By.XPATH, "//a[normalize-space()=\"Sell\"]").click()
time.sleep(4)
#river.find_element(By.XPATH,"//div[normalize-space()='For Owner']").click()

driver.find_element(By.XPATH,"//ul[@class='drop-links']//li//a[@href=\"https://post.magicbricks.com\"]").click()
#time.sleep(4)

