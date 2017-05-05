# Credit to tutorial from http://accraze,info/selenium-tests-with-behave-bdd/
from selenium import webdriver
import flaskr
from flaskr import app

class Browser(object):

    base_url = 'http://127.0.0.1:5000'
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

def close(self):
    self.driver.quit()

def visit(self, location=''):
    url = self.base_url + location
    self.driver.get(url)

def find_by_id(self, selector):
    return self.driver.find_element_by_id(selector)