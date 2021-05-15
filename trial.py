from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def find_hosp(city):
    driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.google.com/maps/@16.7559759,81.6802045,15z")
    driver.implicitly_wait(15)
    #sleep(10)
    str = "hospitals in {}".format(city)
    driver.find_element_by_id("searchboxinput").send_keys(str)
    driver.find_element_by_id("searchbox-searchbutton").click()
    # print(driver.current_url)
    sleep(5)
    driver.close()
    return driver.current_url

