# selenium-demo-py/tests/test_google_search.py
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as match
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver: WebDriver | None


def setup_function():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def teardown_function():
    driver.quit()


def test_google_finds_selene():
    driver.get('https://google.com/ncr')
    WebDriverWait(driver, 4).until(match.presence_of_element_located((By.NAME, 'q')))
    assert driver.find_element(By.NAME, 'q').get_attribute('value') == ''

    driver.find_element(By.NAME, 'q').send_keys('github yashaka selene')
    driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)
    WebDriverWait(driver, 4).until(match.presence_of_element_located((By.CSS_SELECTOR, '#rso>div')))
    assert len(driver.find_elements(By.CSS_SELECTOR, '#rso>div')) >= 6
    assert 'yashaka/selene' in driver.find_elements(By.CSS_SELECTOR, '#rso>div')[0].text

    driver.find_elements(By.CSS_SELECTOR, '#rso>div')[0].find_element(By.CSS_SELECTOR, 'h3').click()
    WebDriverWait(driver, 4).until(match.title_contains('GitHub - yashaka/selene'))
