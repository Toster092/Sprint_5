from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestStellarBurger:
    def test_login_main_success(self, driver):
      driver.find_element(*TestLocators.LOGIN_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.EMAIL_FIELD_LOCATOR).send_keys('alexsolovev11777@gmail.com')
      driver.find_element(*TestLocators.PASSWORD_FIELD_LOCATOR).send_keys('123456')
      driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON_LOCATOR).click()
      WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
          (TestLocators.ORDER_BUTTON_LOCATOR)))
      assert driver.find_element(*TestLocators.ORDER_BUTTON_LOCATOR).text == 'Оформить заказ'

    def test_login_lk_success(self, driver):
      driver.find_element(*TestLocators.ACCOUNT_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.EMAIL_FIELD_LOCATOR).send_keys('alexsolovev11777@gmail.com')
      driver.find_element(*TestLocators.PASSWORD_FIELD_LOCATOR).send_keys('123456')
      driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON_LOCATOR).click()
      WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
          (TestLocators.ORDER_BUTTON_LOCATOR)))
      assert driver.find_element(*TestLocators.ORDER_BUTTON_LOCATOR).text == 'Оформить заказ'

    def test_login_reg_form_success(self, driver):
      driver.find_element(*TestLocators.LOGIN_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.REGISTER_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.LOGIN_IN_REGISTER_LOCATOR).click()
      driver.find_element(*TestLocators.EMAIL_FIELD_LOCATOR).send_keys('alexsolovev11777@gmail.com')
      driver.find_element(*TestLocators.PASSWORD_FIELD_LOCATOR).send_keys('123456')
      driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON_LOCATOR).click()
      WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
          (TestLocators.ORDER_BUTTON_LOCATOR)))
      assert driver.find_element(*TestLocators.ORDER_BUTTON_LOCATOR).text == 'Оформить заказ'

    def test_login_restore_password_success(self, driver):
      driver.find_element(*TestLocators.LOGIN_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.FORGOT_PASSWORD_LOCATOR).click()
      driver.find_element(*TestLocators.FORGOT_PASSWORD_SUBMIT_LOCATOR).click()
      driver.find_element(*TestLocators.EMAIL_FIELD_LOCATOR).send_keys('alexsolovev11777@gmail.com')
      driver.find_element(*TestLocators.PASSWORD_FIELD_LOCATOR).send_keys('123456')
      driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON_LOCATOR).click()
      WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
          (TestLocators.ORDER_BUTTON_LOCATOR)))
      assert driver.find_element(*TestLocators.ORDER_BUTTON_LOCATOR).text == 'Оформить заказ'
