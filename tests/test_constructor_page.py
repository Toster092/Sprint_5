from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestStellarBurger:
  def test_go_to_constructor_success(self, driver):
      driver.find_element(*TestLocators.LOGIN_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.EMAIL_FIELD_LOCATOR).send_keys('alexsolovev11777@gmail.com')
      driver.find_element(*TestLocators.PASSWORD_FIELD_LOCATOR).send_keys('123456')
      driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.ACCOUNT_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.CONSTRUCTION_LOCATOR).click()
      WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
          (TestLocators.BURGER_CONSTRUCTION_TITLE_LOCATOR)))
      assert driver.find_element(*TestLocators.BURGER_CONSTRUCTION_TITLE_LOCATOR).text == 'Соберите бургер'

  def test_go_to_logo_success(self, driver):
      driver.find_element(*TestLocators.LOGIN_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.EMAIL_FIELD_LOCATOR).send_keys('alexsolovev11777@gmail.com')
      driver.find_element(*TestLocators.PASSWORD_FIELD_LOCATOR).send_keys('123456')
      driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.ACCOUNT_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.LOGO_LOCATOR).click()
      WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
          (TestLocators.BURGER_CONSTRUCTION_TITLE_LOCATOR)))
      assert driver.find_element(*TestLocators.BURGER_CONSTRUCTION_TITLE_LOCATOR).text == 'Соберите бургер'