from selenium import webdriver
import time
class GoogleSearch:
    def chrome(self):
        global driver
        driver=webdriver.Chrome(executable_path='D:\\newlib\\chromedriver.exe')
        driver.get('http://google.co.in')
        driver.maximize_window()
        driver.find_element_by_id('lst-ib').send_keys('Mahesh Babu')
        time.sleep(5)
        driver.find_element_by_css_selector('input.lsb').click()
        driver.find_element_by_link_text('Mahesh Babu - Wikipedia').click()

gs=GoogleSearch()
gs.chrome()