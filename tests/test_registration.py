from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
from faker import Faker

faker = Faker()
class TestStellarBurger:
    def test_registration_success(self, driver):
      email = faker.email()
      driver.find_element(*TestLocators.LOGIN_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.REGISTER_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.NAME_FIELD_LOCATOR).send_keys('Jo')
      driver.find_element(*TestLocators.EMAIL_FIELD_LOCATOR).send_keys(email)
      driver.find_element(*TestLocators.PASSWORD_FIELD_LOCATOR).send_keys(Constants.PASSWORD)
      driver.find_element(*TestLocators.REGISTER_SUBMIT_BUTTON_LOCATOR).click()
      WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((TestLocators.LOGIN_SUBMIT_BUTTON_LOCATOR)))
      assert driver.find_element(*TestLocators.LOGIN_TITLE_LOCATOR).text == 'Вход'
    def test_wrong_password_message(self, driver):
      driver.find_element(*TestLocators.LOGIN_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.REGISTER_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.NAME_FIELD_LOCATOR).send_keys('Jo')
      driver.find_element(*TestLocators.EMAIL_FIELD_LOCATOR).send_keys(Constants.EMAIL)
      driver.find_element(*TestLocators.PASSWORD_FIELD_LOCATOR).send_keys('12345')
      driver.find_element(*TestLocators.REGISTER_SUBMIT_BUTTON_LOCATOR).click()
      WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.PASSWORD_ERROR_LOCATOR)))
      assert driver.find_element(*TestLocators.PASSWORD_ERROR_LOCATOR).text == 'Некорректный пароль'
