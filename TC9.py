from selenium.webdriver.common.by import By


class Sell:

    def __init__(self, driver):
        self.driver = driver

    def get_access_to_website(self):
        return self.driver.get("https://www.magicbricks.com/")

    def get_sell(self):
        return self.driver.find_element(By.LINK_TEXT, "Sell").click()

    #def get_post_prop(self):
        #return self.driver.find_element(By.XPATH,"//ul[@class='drop-links']//li//a[@href=\"https://post.magicbricks.com\"]").click()
    def get_access_to_property(self):
        return self.driver.get("https://post.magicbricks.com/")

    def get_ab(self):
        return self.driver.find_element(By.CSS_SELECTOR,".pp-form__fieldset__wrap:nth-child(5) > .pp-form__elem-radio:nth-child(1) > .pp-form__elem-radio__label").click()

    def get_bc(self):
        return self.driver.find_element(By.CSS_SELECTOR,".pp-form__fieldset__wrap:nth-child(2) > .pp-form__elem-radio:nth-child(1) > .pp-form__elem-radio__label").click()

    def get_cd(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".pp-form__label").click()

    def get_de(self):
        return self.driver.find_element(By.ID, "ownerMobile").send_keys("8328419354")

    def get_ef(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".pp-form__cta")

    def get_del(self):
        return self.driver.delete_all_cookies()

    def get_fg(self):
        return self.driver.find_element(By.LINK_TEXT, "Ad Packages").click()

    def get_gh(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#userTypeList > .active > label").click()

    def get_hi(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#sellId > label").click()

    def get_ij(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".m-t-10:nth-child(4) .active > label").click()

    def get_jk(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

    def get_kl(self):
        return self.driver.find_element(By.LINK_TEXT, "Buy Now").click()

    def get_lm(self):
        return self.driver.find_element(By.LINK_TEXT, "Add to My Orders").click()

    def get_mn(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".orderNoArrow").click()

    def get_no(self):
        return self.driver.find_element(By.LINK_TEXT,"iAdvantage").click()

    def get_op(self):
        return self.driver.find_element(By.LINK_TEXT, "Add to My Orders").click()

    def get_pq(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".orderNoArrow").click()

    def get_qr(self):
        return self.driver.get("https://www.magicbricks.com/Real-estate-property-top-agents/agent-in-Mumbai?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Mumbai&mbTrackSrc=tabChange&page=1&category=S")

    def get_rs(self):
        return self.driver.find_element(By.ID, "cityList").click()

    def get_st(self):
        return self.driver.find_element(By.ID, "cityList")

    def get_tu(self):
        return self.driver.find_element(By.XPATH, "//option[. = 'Pune']").click()

    def get_uv(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".srpSort").click()

    def get_vw(self):
        return self.driver.find_element(By.ID, "localityList").click()

    def get_wx(self):
        return self.driver.find_element(By.ID, "localityList")

    def get_xy(self):
        return self.driver.find_element(By.XPATH, "//option[. = 'Hinjewadi']").click()

    def get_yz(self):
        return self.driver.find_element(By.LINK_TEXT, "Contact Agent").click()

    def get_abc(self):
        return self.driver.execute_script("window.scrollTo(0,16.66666603088379)")

    def get_bcd(self):
        return self.driver.find_elements(By.ID, "contactObjButton")

