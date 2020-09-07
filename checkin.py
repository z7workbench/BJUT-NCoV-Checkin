from selenium import webdriver
import argparse
import os
from json import load


def get_user_pass(args):
    if os.path.isfile('./userpass.json'):
        print('Detected JSON file, loading...')
        with open('./userpass.json', 'r') as f:
            js = load(f)
        if js['user'] is None or js['pass'] is None:
            print('Cannot find data, use args instead')
            return args.user, args.password
        else:
            return js['user'], js['pass']
    else:
        print('JSON file is missing, use args instead.')
        return args.user, args.password


def browse(username, password, args):
    if args.dr == 'chrome':
        options = webdriver.ChromeOptions()
        if args.headless:
            options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
    elif args.dr == 'gecko' or args.dr == 'firefox':
        options = webdriver.FirefoxOptions()
        if args.headless:
            options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Firefox(options=options)
    else:
        print('Invalid driver name, use "--driver=gecko" or "--driver=chrome" instead. ')
        return
    login_url = 'https://itsapp.bjut.edu.cn/uc/wap/login'
    ncov_default = 'https://itsapp.bjut.edu.cn/ncov/wap/default/index'

    driver.get(login_url)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/input').send_keys(username)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/input').send_keys(password)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]').click()
    driver.get(ncov_default)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[4]/ul/li[7]/div/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[5]/div/a').click()
    # Missing one click!!
    # driver.find_element_by_xpath('').click()
    driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', type=str)
    parser.add_argument('-p', '--password', type=str)
    parser.add_argument('-d', '--driver', required=True, type=str)
    parser.add_argument('--headless', action='store_false')
    args = parser.parse_args()
    username, password = get_user_pass(args)
    if username is None or password is None:
        print('What?? Why don\'t you enter name and password?? You are a genius! ')
        exit(1)
    browse(username, password, args)
