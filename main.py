import time

import undetected_chromedriver as webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions()
profile = "C:\\Users\\ronit\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
options.add_argument(f"user-data-dir={profile}")
driver = webdriver.Chrome(options=options,use_subprocess=True)

driver.get('https://web.snapchat.com/')
driver.set_window_size(500, 1000)
time.sleep(5)


def main():
    #driver.find_element("xpath",'//*[contains(concat( " ", @class, " " ), concat( " ", "kNGkZ", " " ))]').click()
    time.sleep(0.09)
    driver.find_element("xpath",'//*[contains(concat( " ", @class, " " ), concat( " ", "FBYjn gK0xL A7Cr_ m3ODJ", " " ))]').click()
    time.sleep(0.09)
    driver.find_element("xpath",'//*[contains(concat( " ", @class, " " ), concat( " ", "eiRwx eKaL7", " " ))]').click()
    time.sleep(0.09)
    driver.find_element("xpath",'(//*[contains(concat( " ", @class, " " ), concat( " ", "A8BRr", " " ))])[1]').click()
    driver.find_element("xpath",'(//*[contains(concat( " ", @class, " " ), concat( " ", "A8BRr", " " ))])[2]').click()
    driver.find_element("xpath",'(//*[contains(concat( " ", @class, " " ), concat( " ", "A8BRr", " " ))])[3]').click()
    driver.find_element("xpath",'//*[contains(concat( " ", @class, " " ), concat( " ", "b_WoS", " " ))]').click()
    time.sleep(0.09)


while True:
    try:
        main()
    except Exception as e:
        driver.get('https://web.snapchat.com/')
        driver.set_window_size(500, 1000)
        time.sleep(5)





