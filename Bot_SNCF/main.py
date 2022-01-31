import time
from cv2 import waitKey

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('Bot_SNCF\Ressources\chromedriver.exe')  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bySelection"]/div[3]')))
element.click()
time.sleep(3) # Let the user actually see something!
driver.switch_to.alert().dismiss()






driver.quit()