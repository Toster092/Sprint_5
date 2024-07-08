from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestStellarBurger:
    def test_registration_success(self, driver):
      driver.find_element(*TestLocators.LOGIN_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.REGISTER_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.NAME_FIELD_LOCATOR).send_keys('J')
      driver.find_element(*TestLocators.EMAIL_FIELD_LOCATOR).send_keys('newby33777@gmail.com')
      driver.find_element(*TestLocators.PASSWORD_FIELD_LOCATOR).send_keys('123456')
      driver.find_element(*TestLocators.REGISTER_SUBMIT_BUTTON_LOCATOR).click()
      WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((TestLocators.LOGIN_SUBMIT_BUTTON_LOCATOR)))
      assert driver.find_element(*TestLocators.LOGIN_TITLE_LOCATOR).text == 'Вход'
    def test_wrong_password_message(self, driver):
      driver.find_element(*TestLocators.LOGIN_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.REGISTER_BUTTON_LOCATOR).click()
      driver.find_element(*TestLocators.NAME_FIELD_LOCATOR).send_keys('Jo')
      driver.find_element(*TestLocators.EMAIL_FIELD_LOCATOR).send_keys('alexsolovev11777@gmail.com')
      driver.find_element(*TestLocators.PASSWORD_FIELD_LOCATOR).send_keys('12345')
      driver.find_element(*TestLocators.REGISTER_SUBMIT_BUTTON_LOCATOR).click()
      WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.PASSWORD_ERROR_LOCATOR)))
      assert driver.find_element(*TestLocators.PASSWORD_ERROR_LOCATOR).text == 'Некорректный пароль'
