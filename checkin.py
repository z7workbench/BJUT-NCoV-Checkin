from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import argparse
import time
import os
from json import load
from utils import login


def get_user_pass(args):
    if os.path.isfile('./userpass.json'):
        print('Detected JSON file, loading...')
        with open('./userpass.json', 'r') as f:
            js = load(f)
        if js['user'] is None or js['pass'] is None:
            print('Cannot find data, use args instead')
            return args.username, args.password
        else:
            print('Load completed.')
            return js['user'], js['pass']
    else:
        print('JSON file is missing, use args instead.')
        return args.username, args.password


def browse(username, password, args):
    # configure the driver
    if args.driver == 'chrome':
        options = webdriver.ChromeOptions()
        if args.headless:
            options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
    elif args.driver == 'gecko' or 'firefox':
        options = webdriver.FirefoxOptions()
        if args.headless:
            options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Firefox(options=options)
    # TODO Edge support
    # elif args.driver == 'edge' or 'edgehtml':
    #     driver = webdriver.Edge()
    else:
        print('Invalid driver name, use "--driver=gecko", "--driver=firefox", "--driver=chrome"')
              # '"--driver=edge" or "--driver=edgehtml" instead. ')
        return
    ncov_default = 'https://itsapp.bjut.edu.cn/ncov/wap/default/index'
    # log in the account
    login(driver, username, password)
    time.sleep(2)
    # enter the page
    driver.get(ncov_default)
    # click the location input
    driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[4]/ul/li[7]/div/input').click()
    # wait some time then click the submit button
    try:
        element = WebDriverWait(driver, 5, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/section/div[5]/div/a'))
        )
    except ElementClickInterceptedException:
        driver.quit()
        print('failed!')
        return
    # TODO: Daily Report can only be submitted once a day. You have already submitted
    time.sleep(1)
    element.click()
    # confirm
    try:
        element = WebDriverWait(driver, 5, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div[2]'))
        )
    except ElementClickInterceptedException:
        driver.quit()
        print('failed!')
        return
    time.sleep(1)
    element.click()
    print('Success!')
    driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', type=str,
                        help='Enter your user name.')
    parser.add_argument('-p', '--password', type=str,
                        help='Enter your password, this program will not store your password.')
    parser.add_argument('-d', '--driver', required=True, type=str,
                        help='Choose your driver, Available choices: "chrome" for chromedriver,'
                             '"firefox" or "gecko" for geckodriver (Firefox), "edge" for '
                             'Chromium Microsoft Edge, "edgehtml" for Legacy Edge.')
    parser.add_argument('--headless', action='store_true',
                        help='Use Headless web browser. If you want to see the browser window, '
                             'do not use this argument. This argument is invalid when using '
                             'Edge.')
    args = parser.parse_args()
    username, password = get_user_pass(args)
    if username is None or password is None:
        print('What?? Why don\'t you enter name and password?? You are a genius! ')
        exit(1)
    browse(username, password, args)
