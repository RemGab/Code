import time
from click import option
from cv2 import waitKey

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1100,1000")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')

driver = webdriver.Chrome(options=options, executable_path='Bot_SNCF\Ressources\chromedriver.exe')  # Optional argument, if not specified will search path.

driver.get('https://www.sncf-connect.com/app/account')

wait = WebDriverWait(driver, 10)
try:
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bySelection"]/div[3]')))
    element.click()
except:
    pass

try:
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="L2AGLb"]/div')))
    element.click()
except:
    pass

time.sleep(10)

driver.quit()