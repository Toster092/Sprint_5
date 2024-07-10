from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
class TestStellarBurger:
  def test_logout_success(self, driver):
      driver.find_element(*TestLocators.LOGIN_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.EMAIL_FIELD_LOCATOR).send_keys(Constants.EMAIL)
      driver.find_element(*TestLocators.PASSWORD_FIELD_LOCATOR).send_keys(Constants.PASSWORD)
      driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON_LOCATOR).click()
      WebDriverWait(driver, 7).until(
          expected_conditions.element_to_be_clickable((TestLocators.ACCOUNT_BUTTON_LOCATOR)))
      driver.find_element(*TestLocators.ACCOUNT_BUTTON_LOCATOR).click()
      WebDriverWait(driver, 7).until(
          expected_conditions.element_to_be_clickable((TestLocators.LOGOUT_LOCATOR)))
      driver.find_element(*TestLocators.LOGOUT_LOCATOR).click()
      WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable(
          (TestLocators.LOGIN_AFTER_LOGOUT_LOCATOR)))
      assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'