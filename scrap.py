from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.headless = True


# driver = webdriver.Firefox(executable_path="C://chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)


def get_doctors(city, pincode):
    t1 = time.perf_counter()
    #driver = webdriver.Chrome(options=chromeOptions)
    driver = webdriver.Chrome()
    driver.get("https://www.justdial.com/{}/General-Physician-Doctors-in-{}/nct-10892680".format(city, pincode))
    while True:
        try:
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/section[16]/section/span").click()
            break
        except Exception:
            pass
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    items = {}
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    for count in range(100):
        card = driver.find_element_by_xpath('//*[@id="bcard{}"]/div[1]'.format(count))
        names_selector = soup.select_one('#bcard{} > div.col-md-12.col-xs-12.colsp > section > div.col-sm-5.col-xs-8.store-details.sp-detail.paddingR0 > h2 > span > a > span'.format(count))
        if names_selector == None:
            name = 'Not Avaialble'
        else:
            name = names_selector.text
        image_selector = card.find_element_by_xpath('//*[@id="newphoto{}"]/img'.format(count))
        if image_selector == None:
            image = 'Not Avaialble'
        else:
            image = image_selector.get_attribute("src")
        address_selector = soup.select_one('#morehvr_add_cont{} > span.cont_fl_addr'.format(count))
        if address_selector == None:
            address = 'Not Avaialble'
        else:
            address = address_selector.text
        
        ratings_selector = soup.select_one('#bcard{} > div.col-md-12.col-xs-12.colsp > section > div.col-sm-5.col-xs-8.store-details.sp-detail.paddingR0 > p.newrtings > a > span.green-box'.format(count))
        if ratings_selector == None:
            rating = 'Not Avaialble'
        else:
            rating = ratings_selector.text

        items[name] = {"name":  name, "image": image, "rating": rating, "address": address}
    driver.quit()
    print("Time taken : ",time.perf_counter() - t1)
    return items