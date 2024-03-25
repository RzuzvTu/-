from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
#【ROF-MAO 1st LIVE】ペンライト
#driver.get("https://shop.nijisanji.jp/s/niji/item/detail/SSZS-30075?ima=0948")
#【ROF-MAO 1st LIVE】ペンライト
buy1 = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[6]/ul/li/div[2]/div[2]/div/button')))
buy1.click()
for i in range(4):
    add = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[6]/ul/li/div[2]/div[2]/div/div/button[2]')))
    add.click()
time.sleep(2)
#【ChroNoiR One-Man Live】ペンライト
driver.get("https://shop.nijisanji.jp/s/niji/item/detail/SSZS-29397?ima=0948")
#【ChroNoiR One-Man Live】ペンライト
buy1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[6]/ul/li/div[2]/div[2]/div/button')))
buy1.click()
for i in range(4):
    add = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[6]/ul/li[2]/div[2]/div[2]/div/div/button[2]')))
    add.click()
time.sleep(2)
#【ChroNoiR One-Man Live】ペンライトリボン
driver.get("https://shop.nijisanji.jp/s/niji/item/detail/SSZS-29388?ima=0948")
#【ChroNoiR One-Man Live】ペンライトリボン 叶
buy1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[6]/ul/li[1]/div[2]/div[2]/div/button')))
buy1.click()
buy2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[6]/ul/li[2]/div[2]/div[2]/div/button')))
buy2.click()
for i in range(4):
    add1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[6]/ul/li[1]/div[2]/div[2]/div/div/button[2]')))
    add1.click()
    add2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[6]/ul/li[2]/div[2]/div[2]/div/div/button[2]')))
    add2.clicka()
time.sleep(2)
#【ROF-MAO 1st LIVE】アクリルスタンド
driver.get("https://shop.nijisanji.jp/s/niji/item/detail/SSZS-30069?ima=3229")
#【ROF-MAO 1st LIVE】アクリルスタンド 剣持刀也
buy1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[6]/ul/li[2]/div[2]/div[2]/div/button')))
buy1.click()
#【ROF-MAO 1st LIVE】アクリルスタンド 不破湊                              
buy2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[6]/ul/li[3]/div[2]/div[2]/div/button')))
buy2.click()
for i in range(4):
    add1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[6]/ul/li[2]/div[2]/div[2]/div/div/button[2]')))
    add1.click()                                                           
    add2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[6]/ul/li[3]/div[2]/div[2]/div/div/button[2]')))
    add2.click()
time.sleep(3)
storecar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="VUE_APP_ROOT"]/div/div/header/div[1]/div/nav/div[1]/form[2]/button')))
storecar.click()