from selenium import webdriver
from selenium.webdriver.common.by import By
import time

vars = {}
from selenium import webdriver
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
driver = webdriver. Chrome()
driver.maximize_window()
driver.get("https://www.magicbricks.com/")
driver.find_element(By.LINK_TEXT, "Sell").click()
#driver.find_element(By.XPATH,"//div[normalize-space()='For Owner']").click()
#driver.find_element(By.XPATH,"//ul[@class='drop-links']//li//a[@href='https://post.magicbricks.com']").click()
time.sleep(6)

#driver.get("https://post.magicbricks.com/")

driver.find_element(By.XPATH,"(//a[@href='https://post.magicbricks.com'])[2]").click()
time.sleep(5)
child_window_handle = driver.window_handles[-1]
driver.switch_to.window(child_window_handle)

driver.find_element(By.CSS_SELECTOR,
                    ".pp-form__fieldset__wrap:nth-child(5) > .pp-form__elem-radio:nth-child(1) > .pp-form__elem-radio__label").click()
driver.find_element(By.CSS_SELECTOR,
                    ".pp-form__fieldset__wrap:nth-child(2) > .pp-form__elem-radio:nth-child(1) > .pp-form__elem-radio__label").click()
driver.find_element(By.CSS_SELECTOR, ".pp-form__label").click()
driver.find_element(By.ID, "ownerMobile").send_keys("8328419354")
time.sleep(5)
elements = driver.find_elements(By.CSS_SELECTOR, ".pp-form__cta")
assert len(elements) > 0

driver.quit()
