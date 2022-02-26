import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="module")
def firefox_driver():

    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    settings = webdriver.FirefoxOptions()
    settings.add_argument("-private")
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=settings)
    url = "https://radiothek.orf.at/search"
    driver.get(url)
    expectation = EC.presence_of_element_located((By.ID, "didomi-notice-agree-button"))
    element = WebDriverWait(driver, 10).until(expectation)
    element.click()
    time.sleep(2)
    yield driver

    driver.quit()

def test_1(firefox_driver):
    search_item = "Mozart"
    search_element = firefox_driver.find_element(By.CSS_SELECTOR, "input[type=search]")
    search_element.send_keys(search_item)
    result_is_present = EC.presence_of_element_located((By.CSS_SELECTOR, ".search-has-query h2"))
    result_header_element = WebDriverWait(firefox_driver, 10).until(result_is_present)

    assert result_header_element.text == f'Suchergebnis für "{search_item}"'

def test_2(firefox_driver):
    results= firefox_driver.find_elements(By.XPATH, '//span[@class="type"]')
    assert len (results) > 1
