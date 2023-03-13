import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
vars = {}

driver.maximize_window()
driver.get("https://www.magicbricks.com/")
driver.find_element(By.LINK_TEXT, "Sell").click()
time.sleep(5)
#driver.get("https://www.magicbricks.com/Real-estate-property-top-agents/agent-in-Mumbai?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Mumbai&mbTrackSrc=tabChange&page=1&category=S")
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[3]/div/div/div[3]/ul/li[2]/a").click()
time.sleep(4)
child_window_handle = driver.window_handles[-1]
driver.switch_to.window(child_window_handle)
dropdown = driver.find_element(By.ID, "cityList")
time.sleep(3)
dropdown.find_element(By.XPATH, "//option[. = 'Pune']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".srpSort").click()
time.sleep(3)
driver.find_element(By.ID, "localityList").click()
time.sleep(3)
dropdown = driver.find_element(By.ID, "localityList")
time.sleep(3)
dropdown.find_element(By.XPATH, "//option[. = 'Hinjewadi']").click()
time.sleep(3)

vars["window_handles"] = driver.window_handles

driver.find_element(By.LINK_TEXT, "Contact Agent").click()
driver.execute_script("window.scrollTo(0,16.66666603088379)")
elements = driver.find_elements(By.ID, "contactObjButton")
assert len(elements) > 0