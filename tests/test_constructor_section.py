from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestStellarBurger:
  def test_go_to_bulki_success(self, driver):
      driver.find_element(*TestLocators.SOUSSES_TAB_LOCATOR).click()
      driver.find_element(*TestLocators.BURGERS_TAB_LOCATOR).click()
      WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
          (TestLocators.FLUORESCENT_BURGER_LOCATOR)))
      assert driver.find_element(*TestLocators.FLUORESCENT_BURGER_LOCATOR).text == 'Флюоресцентная булка R2-D3'

  def test_go_to_souses_success(self, driver):
      driver.find_element(*TestLocators.SOUSSES_TAB_LOCATOR).click()
      WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
          (TestLocators.SOUSSE_SPIKY_X_LOCATOR)))
      assert driver.find_element(*TestLocators.SOUSSE_SPIKY_X_LOCATOR).text == 'Соус Spicy-X'

  def test_go_to_ingridients_success(self, driver):
      driver.find_element(*TestLocators.INGREDIENTS_TAB_LOCATOR).click()
      WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
          (TestLocators.LIGHTNING_FILE_LOCATOR)))
      assert driver.find_element(*TestLocators.LIGHTNING_FILE_LOCATOR).text == 'Филе Люминесцентного тетраодонтимформа'
