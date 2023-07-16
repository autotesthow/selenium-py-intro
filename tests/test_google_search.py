# selenium-py-intro/tests/test_google_search.py


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager








driver: WebDriver | None


def setup_module():

    installation_path = ChromeDriverManager().install()
    global driver; driver = webdriver.Chrome(service=ChromeService(installation_path))



def teardown_module():

    driver.quit()



def test_google_finds_selene():

    driver.get('https://google.com/ncr')
    assert driver.find_element(By.NAME, 'q').get_attribute('value') == ''

    driver.find_element(By.NAME, 'q').send_keys('github yashaka selene')
    driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)
    assert len(driver.find_elements(By.CSS_SELECTOR, '#rso>div')) >= 5
    assert 'yashaka/selene' in driver.find_elements(By.CSS_SELECTOR, '#rso>div')[0].text

    driver.find_elements(By.CSS_SELECTOR, '#rso>div')[0].find_element(By.CSS_SELECTOR, 'h3').click()
    assert 'GitHub - yashaka/selene' in driver.title

