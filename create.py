import sys
import os
from selenium import webdriver

path = "/home/elabs/Downloads/myProjects"
browser = webdriver.Chrome()
browser.get('https://github.com/login')

def create():
    folderName = str(sys.argv[1])
    #os.maked(path + folderName)
    python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
    python_button.send_keys('iCodeElijah')
    python_button = browser.find_elements_by_xpath("//input[@name='password']")[0]
    python_button.send_key('Elijahk.56092')
    python_button = browser.find_elements_by_xpath("//input[@name='commit']")[0]
    python_button.click()
    browser.get('https://github.com/new')
    python_button = browser.find_elements_by_xpath("//input[@name='repository[name]']")[0]
    python_button.send_keys(folderName)
    python_button = browser.find_elements_by_css_selector('button.first-in-line')
    python_button.submit()
    browser.quit()
    #python_button.click()
if __name__ == "__main__":
    create()
    
