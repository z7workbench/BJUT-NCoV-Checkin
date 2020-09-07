from selenium import webdriver
import argparse
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
            return js['user'], js['pass']
    else:
        print('JSON file is missing, use args instead.')
        return args.username, args.password


def browse(username, password, args):
    if args.driver == 'chrome':
        options = webdriver.ChromeOptions()
        if args.headless:
            options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
    elif args.driver == 'gecko' or args.driver == 'firefox':
        options = webdriver.FirefoxOptions()
        if args.headless:
            options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Firefox(options=options)
    else:
        print('Invalid driver name, use "--driver=gecko" or "--driver=chrome" instead. ')
        return
    ncov_default = 'https://itsapp.bjut.edu.cn/ncov/wap/default/index'
    login(driver, username, password)
    driver.get(ncov_default)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[4]/ul/li[7]/div/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[5]/div/a').click()
    # Missing one click!!
    # driver.find_element_by_xpath('').click()
    driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', type=str,
                        help='Enter your user name.')
    parser.add_argument('-p', '--password', type=str,
                        help='Enter your password, this program will not store your password.')
    parser.add_argument('-d', '--driver', required=True, type=str,
                        help='Choose your driver, Available choices: "chrome" for chromedriver,'
                             '"firefox" or "gecko" for geckodriver (Firefox).')
    parser.add_argument('--headless', action='store_false',
                        help='Use Headless web browser. If you want to see the browser window, '
                             'do not use this argument.')
    args = parser.parse_args()
    username, password = get_user_pass(args)
    if username is None or password is None:
        print('What?? Why don\'t you enter name and password?? You are a genius! ')
        exit(1)
    browse(username, password, args)
