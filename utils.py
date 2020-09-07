def login(driver, username, password):
    login_url = 'https://itsapp.bjut.edu.cn/uc/wap/login'
    driver.get(login_url)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/input').send_keys(username)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/input').send_keys(password)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]').click()
    print('Login completed')
