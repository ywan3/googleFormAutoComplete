import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import *
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
def google_login_handler(driver):
    username = "wyj33wyj@gmail.com"
    password = "wyj33wyj680904"
    stackoverflow_login_bypass(driver, username, password)

    url = 'https://accounts.google.com/v3/signin/identifier?dsh=S-318575229%3A1668389932759552&continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSd-rM6m4dVEwI11kAVilYo7L9iBHyvng42YnHBUfPteC4kUug%2Fviewform%3Fvc%3D0%26c%3D0%26w%3D1%26flr%3D0&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSd-rM6m4dVEwI11kAVilYo7L9iBHyvng42YnHBUfPteC4kUug%2Fviewform%3Fvc%3D0%26c%3D0%26w%3D1%26flr%3D0&ltmpl=forms&passive=1209600&service=wise&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=ARgdvAuVgMwb6zKBlO9cagYZed7ZNx_-puV3BO4mCWXFdxVLiODjUeQ6V6a35P09mJPmb5lyxF-t5w'
    driver.get(url)

    driver.find_element(By.ID, "identifierId").send_keys('wyj33wyj@gmail.com')
    driver.find_element(By.ID, "identifierNext").click()
    driver.find_element(By.Class, "whsOnd zHQkBf").send_keys(os.environ['wyj33wyj680904'])
    driver.find_element(By.Class, "VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b").click()

def stackoverflow_login_bypass(driver, username, password):

    
    driver.get('https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="openid-buttons"]/button[1]').click()
    driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(username)

    sleep(3)

    driver.find_element(By.XPATH, '//*[@id="identifierNext"]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]').click()
    sleep(2)
    driver.get('https://youtube.com')
    sleep(5)


google_login_handler(driver)