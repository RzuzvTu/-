from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
__path__ = "C:/Users/taian/OneDrive/Desktop/driver/chromedriver.exe"
driver = webdriver.Chrome()
driver.get('https://shop.nijisanji.jp/s/niji/?ima=5856')
search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'form-control')))
search.send_keys("Meloco")
search.send_keys(Keys.RETURN)
go = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, '【バレンタイングッズ2024】アクリルスタンド')))
go.click()
buy = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[7]/div[2]/div[2]/div/button')))
buy.click()
for i in range(4):
    add = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[7]/div[2]/div[2]/div/div/button[2]')))
    add.click()
buy = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[3]/div[2]/div[2]/div[2]/button')))
buy.click()
for i in range(4):
    add = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[3]/div[2]/div[2]/div[2]/div/button[2]')))
    add.click()
time.sleep(2)
driver.execute_script("window.scrollTo(10, document.body.scrollHeight)")
time.sleep(1)
nextbuy = driver.find_element(By.XPATH,'//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/form/button')
nextbuy.click()
buy = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/main/div/div[1]/div[5]/form/button')))
buy.click()
time.sleep(5)