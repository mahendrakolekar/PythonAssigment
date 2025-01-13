import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.Locators.Locators import Locators

class CreateOpportunity(Locators):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def create_opportunity(self, opportunity_name, existing_account,close_date,stage,forecast_category):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.driver.find_element(By.XPATH, self.opportunities_tab)).click().perform()
            time.sleep(8)
            action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, self.new_button)).click().perform()
            time.sleep(5)
            # Fill out the opportunity form
            self.driver.find_element(By.XPATH, self.opportunity_name).send_keys(opportunity_name)
            self.driver.find_element(By.XPATH, self.select_account_name).send_keys(existing_account)
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.select_account_name).click()
            action.move_to_element(self.driver.find_element(By.XPATH, self.account_option.format(existing_account))).click().perform()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.close_date).send_keys(close_date)
            element1 = self.driver.find_element(By.XPATH, self.stage)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element1)
            element1.click()
            time.sleep(3)
            action.move_to_element(self.driver.find_element(By.XPATH, self.select_stage_option.format(stage))).click().perform()
            time.sleep(2)
            element2 = self.driver.find_element(By.XPATH, self.forecast_category)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element2)
            element2.click()
            time.sleep(2)
            action.move_to_element(self.driver.find_element(By.XPATH, self.forecast_category_option.format(forecast_category))).click().perform()
            # Save the opportunity
            self.logger.info("Saving the opportunity")
            self.driver.find_element(By.XPATH, self.save_button).click()
            time.sleep(10)

            self.logger.info("opportunity saved successfully")

        except Exception as e:
            self.logger.error(f"Error occurred while creating a opportunity: {e}")
            self.driver.save_screenshot("create_opportunity__capture_error.png")
            raise
    def verify_opportunity_has_saved(self, opportunity_name,existing_account):
        # Verifying opportunity has saved
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.account_tab)).click().perform()
        time.sleep(2)
        action.move_to_element(self.driver.find_element(By.XPATH, self.existing_account.format(existing_account))).click().perform()
        time.sleep(2)
        element = self.driver.find_element(By.XPATH, self.verify_contact_or_opportunity.format(opportunity_name))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element.text