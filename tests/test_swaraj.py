from selenium.webdriver.common.by import By

def test_example(driver):
    driver.get("https://demoqa.com/")
    assert "DEMOQA1" in driver.title

def test_clickElements(driver):
    print(driver.current_url)
    assert driver.current_url in driver.current_url


