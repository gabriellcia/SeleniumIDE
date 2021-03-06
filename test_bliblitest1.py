# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBliblitest1():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_bliblitest1(self):
    self.driver.get("https://www.blibli.com/")
    self.driver.set_window_size(1062, 672)
    self.driver.find_element(By.NAME, "search").click()
    self.driver.find_element(By.NAME, "search").send_keys("iphone 13")
    self.driver.find_element(By.CSS_SELECTOR, ".searchbox__search > img").click()
    self.driver.find_element(By.NAME, "search").click()
    self.driver.find_element(By.NAME, "search").click()
    self.driver.find_element(By.CSS_SELECTOR, ".searchbox__search").click()
    self.driver.find_element(By.CSS_SELECTOR, ".searchbox__action > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".title").click()
    self.driver.find_element(By.CSS_SELECTOR, ".skeleton-container__left__main-filter__filters:nth-child(1) > .filter-content:nth-child(4)").click()
    self.driver.find_element(By.NAME, "search").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active > div").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".searchbox__search")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".searchbox__search").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, "#seller > .drop-down-filter-label").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .drop-down-container-row > .drop-down-container-row-name").click()
    self.driver.find_element(By.CSS_SELECTOR, ".drop-down-container-buttons-apply").click()
    assert self.driver.title == "Online Mall Blibli.com, Sensasi Belanja Online Shop ala Mall"
    element = self.driver.find_element(By.CSS_SELECTOR, ".cart__amt")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
  
