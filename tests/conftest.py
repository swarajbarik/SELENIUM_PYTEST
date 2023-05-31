import html
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    request.addfinalizer(driver.quit)
    driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

