from selenium import webdriver
from selenium.webdriver.common.by import By

def test_example():
    # Set up the WebDriver (for example, Chrome)
    driver = webdriver.Chrome()

    # Open a website
    driver.get("https://www.example.com")

    # Perform some actions
    element = driver.find_element(By.XPATH, "//input[@name='q']")
    element.send_keys("pytest with Selenium")

    # Perform assertions
    assert "pytest" in driver.title

    # Close the browser
    driver.quit()

