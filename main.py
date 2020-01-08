from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pyautogui as pgui
import time

driver = webdriver.Firefox(executable_path='./geckodriver')

try:
    driver.get('https://www.e-typing.ne.jp/roma/check/')

    time.sleep(1)
    driver.find_element_by_id('level_check_btn').click()

    time.sleep(3)
    driver.switch_to_frame('typing_content')
    driver.find_element_by_xpath('//*[@id="start_btn"]').click()

    # pgui.keyDown('space')
    driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)

    time.sleep(3.5)

    while True:
        try:
            texts = driver.find_element_by_id('sentenceText').text
            print(texts)

            for text in texts:
                pgui.typewrite(text)

        except Exception:
            break

    # while True:
    #     try:
    #         texts = driver.find_element_by_id('sentenceText').text
    #         print(texts)
    #
    #         for text in texts:
    #             time.sleep(0.1)
    #             driver.find_element_by_tag_name('body').send_keys(text)
    #
    #     except Exception:
    #         break

except Exception:
    pass
    # driver.quit()
    # driver.close()

