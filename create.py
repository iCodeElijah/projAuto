import sys
import os
from selenium import webdriver

path = "/home/elabs/Downloads/myProjects"
browser = webdriver.Chrome()
browser.get('https://github.com/login')

def create():
    folderName = str(sys.argv[1])
    os.maked(path + folderName)
    python_button = browser.find_element_by_xpath("//*[@id='login_field']")[0]
    python_button.send_keys('iCodeElijah')
    
if __name__ == "__main__":
    create()
    