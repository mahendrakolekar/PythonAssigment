import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from PageObjects.Locators.Locators import Locators

class CreateLead(Locators):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def create_lead(self, salutation, f_name, l_name, company):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.driver.find_element(By.XPATH, self.sales_tab)).click().perform()
            time.sleep(5)
            action.move_to_element(self.driver.find_element(By.XPATH, self.leads_tab)).click().perform()
            time.sleep(5)
            # Click the New Lead button
            self.logger.info(f"Click on  New button")
            action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, self.new_button)).click().perform()
            time.sleep(5)

            # Fill out the lead form
            self.driver.find_element(By.XPATH, self.salutation).click()
            self.driver.find_element(By.XPATH, self.salutation_option.format(salutation)).click()
            self.driver.find_element(By.XPATH, self.first_name).send_keys(f_name)
            self.driver.find_element(By.XPATH, self.last_name).send_keys(l_name)
            self.driver.find_element(By.XPATH, self.company).send_keys(company)

            # Save the lead
            self.logger.info("Saving the lead")
            self.driver.find_element(By.XPATH, self.save_button).click()
            time.sleep(10)

            self.logger.info("The Lead created successfully")

        except Exception as e:
            self.logger.error(f"Error occurred while creating a lead: {e}")
            self.driver.save_screenshot("create_lead_capture_error.png")
            raise