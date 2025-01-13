import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Locators.Locators import Locators


class LoginPage(Locators):
    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username_):
        self.driver.find_element(By.ID, self.username_loc_id).clear()
        self.driver.find_element(By.ID, self.username_loc_id).send_keys(username_)

    def setPassword(self, password_):
        self.driver.find_element(By.ID, self.password_loc_id).clear()
        self.driver.find_element(By.ID, self.password_loc_id).send_keys(password_)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_loc_id).click()