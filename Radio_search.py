import pytest



@pytest.fixture
def firefox_driver():
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager

    settings = webdriver.FirefoxOptions()
    settings.add_argument("-private")
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=settings)
    yield driver

    driver.quit()

def test_1(firefox_driver):
    url = "https://radiothek.orf.at/search"
    firefox_driver.get(url)

    assert firefox_driver.title == "Welcome to Python.org"


