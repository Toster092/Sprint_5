from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
class TestStellarBurger:
  def test_go_to_lk_success(self, driver):
      driver.find_element(*TestLocators.LOGIN_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.EMAIL_FIELD_LOCATOR).send_keys(Constants.EMAIL)
      driver.find_element(*TestLocators.PASSWORD_FIELD_LOCATOR).send_keys(Constants.PASSWORD)
      driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.ACCOUNT_BUTTON_LOCATOR).click()
      WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((TestLocators.ACCOUNT_PROFILE_LOCATOR)))
      assert driver.find_element(*TestLocators.ACCOUNT_PROFILE_LOCATOR).text == 'Профиль'
