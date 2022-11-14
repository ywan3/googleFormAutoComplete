
url = "https://docs.google.com/forms/d/e/1FAIpQLSd-rM6m4dVEwI11kAVilYo7L9iBHyvng42YnHBUfPteC4kUug/viewform?vc=0&c=0&w=1&flr=0"


def answerName(driver, df, element_class):
    name = df['name']
    name_space = driver.find_elements_by_class_name(element_class)
    for a, q in zip(name, name_space):
        q.send_keys(a)

    return driver


def answerGender(driver, df, element_class):
    gender = df['gender']
    driver.find_elements_by_class_name(element_class)[2].click()
    
    return driver


def answerDate(driver, df, element_class):
    return driver



def submit(driver, element_class):
    driver.find_element_by_xpath(element_class).click()
    return driver



def driver_process(driver, name_class, choice_class, date_class, submit_class):
    driver.get(url)

    driver.maximize_window()
    
    driver = answerName(driver, df, name_class)
    driver = answerGender(driver, df, choice_class)
    driver = answerDate(driver, df, date_class)
    driver = driver.submit(driver, submit_class)