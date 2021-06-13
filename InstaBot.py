from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
import time
import random


def hashtag_search(username, password, hashtag):
    browser = webdriver.Chrome()

    try:
        browser.get('https://www.instagram.com')
        time.sleep(1)

        browser.find_element_by_xpath('/html/body/div[2]/div/div/button[1]').click()
        time.sleep(1)

        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)
        time.sleep(1)

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(3)

        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(2)

            hrefs = browser.find_elements_by_tag_name('a')

            post_urls = []
            for item in hrefs:
                href = item.get_attribute('href')

                if '/p/' in href:
                    post_urls.append(href)


            for url in post_urls:
                browser.get(url)
                time.sleep(random.randrange(1))

                browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
                time.sleep(random.randrange(1))

            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


hashtag_search(username, password, 'hashtag')
