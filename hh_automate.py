from selenium import webdriver
from random import randint
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import email, password
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("window-size=1400,2100")
chrome_options.add_argument('--disable-gpu')


def main():
    while True:
        try:
            browser = webdriver.Chrome(
                ChromeDriverManager().install(), chrome_options=chrome_options)
            browser.get('https://hh.ru/account/login?backurl=%2F')
            wait_page_to_load = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div[2]/div/div/form/div[1]/input"))
            )
            find_email_input = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[2]/div/div/form/div[1]/input")
            find_email_input.send_keys(email)
            find_password_input = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[2]/div/div/form/div[3]/input")
            find_password_input.send_keys(password)

            find_submit = browser.find_element_by_xpath(
                '/html/body/div[2]/div/div[2]/div/div/form/div[4]/input')
            find_submit.submit()
            find_cv = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/a[2]/span/span[1]"))
            )
            find_cv.click()
            update_cv = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[6]/div/div/div[3]/div/div/div/div[1]/div[3]/div/div[5]/div/div/div/div[1]/span/button"))
            )
            update_cv.click()

            print('updated')
        except TimeoutException:
            print('Error')
        update_period = 60 * 60 * 4 + 60 * randint(1, 20)
        sleep(float(update_period))


if __name__ == "__main__":
    main()
