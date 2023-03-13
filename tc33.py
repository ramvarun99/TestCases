from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestSha():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def test_sha(self):
        self.driver.get("https://www.magicbricks.com/")
        self.driver.find_element(By.LINK_TEXT, "Sell").click()
        time.sleep(6)
        """
        self.driver.get("https://post.magicbricks.com/")
        """
        self.driver.find_element(By.XPATH,"//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[3]/div/div/div[1]/ul/li[1]/a").click()
        time.sleep(5)
        child_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(child_window_handle)

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".pp-form__fieldset__wrap:nth-child(5) > .pp-form__elem-radio:nth-child(1) > .pp-form__elem-radio__label").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".pp-form__fieldset__wrap:nth-child(2) > .pp-form__elem-radio:nth-child(1) > .pp-form__elem-radio__label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".pp-form__label").click()
        self.driver.find_element(By.ID, "ownerMobile").send_keys("8328419354")
        time.sleep(5)
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".pp-form__cta")
        assert len(elements) > 0

        self.driver.quit()
