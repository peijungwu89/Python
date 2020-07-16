from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.thsrc.com.tw/')

time.sleep(1)
driver.find_element_by_id('select_location01').click()
driver.find_element_by_id('select_location01').send_keys('左營')

time.sleep(1)
driver.find_element_by_id('select_location02').click()
driver.find_element_by_id('select_location02').send_keys('台北')

time.sleep(1)
driver.find_element_by_id('typesofticket').click()
driver.find_element_by_id('typesofticket').send_keys('單程')

time.sleep(1)
driver.find_element_by_id('Departdate01').click()
driver.find_element_by_id('Departdate01').clear()
driver.find_element_by_id('Departdate01').send_keys('2020.07.18')

time.sleep(1)
driver.find_element_by_id('outWardTime').click()
# driver.find_element_by_id('outWardTime').clear()

time.sleep(1.5)
driver.find_element_by_id('outWardTime').send_keys(Keys.CONTROL, 'a')
driver.find_element_by_id('outWardTime').send_keys(Keys.DELETE )
driver.find_element_by_id('outWardTime').send_keys('07:00')


time.sleep(1)
driver.find_element_by_id('start-search').click()

time.sleep(1)
