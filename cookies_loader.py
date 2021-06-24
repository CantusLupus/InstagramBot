from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
import time
import random
import pickle

driver = webdriver.Chrome()

try:
    #    # cookies_load
    # -----------------------------------------------------------------------------------------
    # driver.get('https://www.instagram.com')
    # time.sleep(1)

    # driver.find_element_by_xpath('/html/body/div[3]/div/div/button[1]').click()
    # time.sleep(1)
    #
    # username_input = driver.find_element_by_name('username')
    # username_input.clear()
    # username_input.send_keys(username)
    # time.sleep(1)
    #
    # password_input = driver.find_element_by_name('password')
    # password_input.clear()
    # password_input.send_keys(password)
    #
    # password_input.send_keys(Keys.ENTER)
    # time.sleep(3)
    #
    # pickle.dump(driver.get_cookies(), open(f"{username}_cookies", "wb"))
    # --------------------------------------------------------------------------------
    # verifying

    driver.get('https://www.instagram.com')
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[3]/div/div/button[1]').click()
    time.sleep(1)

    driver.delete_all_cookies()

    for cookie in pickle.load(open(f"{username}_cookies", "rb")):
        driver.add_cookie(cookie)
    time.sleep(3)

    driver.refresh()
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
