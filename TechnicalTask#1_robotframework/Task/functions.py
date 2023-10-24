from selenium import webdriver
from robot.api import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_post_creation(title_text):
    driver = webdriver.Chrome()
    # Capture the current URL
    # Navigate to the desired URL
    url = "https://react-redux.realworld.io/#/article/{title_text}"  # replace with the actual URL or make it dynamic
    driver.get(url)

    # Capture the current URL
    current_url = driver.current_url

    # Check if title_text is in the URL
    if current_url.contains(title_text):
        logger.warn("title_text", title_text)
        logger.warn("current_url", current_url)
        logger.warn(f"Expected '{title_text}' to be in the URL but wasn't found.")
        driver.quit()
        return

    # Create a dynamic XPath using the title_text variable
    xpath_locator = f"//div[@class='container']//h1[text()='{title_text}']"

    logger.warn(xpath_locator)

    # Assert based on page content
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_locator)))
    post_title = element.text
    logger.warn(f"Expected: {title_text}, post_title: {post_title}")

    assert post_title == title_text, f"Expected '{title_text}' but got '{post_title}'"

    driver.quit()