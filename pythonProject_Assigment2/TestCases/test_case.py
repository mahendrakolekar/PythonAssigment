import time

import pytest

from PageObjects.ConvertLead import ConvertLead
from PageObjects.CreateContact import CreateContact
from PageObjects.CreateLead import CreateLead
from PageObjects.CreateOpportunity import CreateOpportunity
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Testcase001:
    pageurl = ReadConfig.get_Application_url()
    username = ReadConfig.get_user_name()
    password = ReadConfig.get_password()


    def test_open_login_page(self, setup):
        self.driver = setup
        self.driver.get(self.pageurl)
        time.sleep(2)


    def test_user_login_into_salesforce(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

    @pytest.mark.parametrize("salutation, f_name, l_name, company", [
        ("Mr.", "John", "Todd", "Acme Corp")
    ])
    def test_create_lead(self, salutation, f_name, l_name, company,setup):
        self.driver = setup
        self.cl = CreateLead(self.driver)
        self.cl.create_lead(salutation, f_name, l_name, company)

    def test_convert_lead(self,setup):
        self.driver = setup
        self.rl = ConvertLead(self.driver)
        self.rl.convert_lead()
        self.rl.go_to_leads_page()

    @pytest.mark.parametrize("salutation, f_name, l_name, existing_contact,contact_name", [
        ("Mr.", "John", "Todd", "Acme Corp", "John Todd")
    ])
    def test_create_contact(self,salutation,f_name,l_name,existing_contact,contact_name,setup):
        self.driver = setup
        self.cc = CreateContact(self.driver)
        self.cc.create_contact(salutation,f_name,l_name,existing_contact)

        text = self.cc.verify_contact_has_saved(contact_name,existing_contact)
        if text == "John Todd":
            assert True
        else:
            assert False

    @pytest.mark.parametrize("opportunity_name,existing_contact,close_date,stage,forecast_category", [
        ("Zaya Opp","Acme Corp","02/2/2025","Propose","Pipeline")
    ])
    def test_create_opportunity(self,opportunity_name,existing_contact,close_date,stage,forecast_category,setup):
        self.driver = setup
        self.cp = CreateOpportunity(self.driver)
        self.cp.create_opportunity(opportunity_name,existing_contact,close_date,stage,forecast_category)

        text = self.cp.verify_opportunity_has_saved(opportunity_name,existing_contact)
        if text == "Zaya Opp":
            assert True
        else:
            assert False

