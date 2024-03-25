#【ROF-MAO 1st LIVE】ホログラム缶バッジ
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
#driver.get("https://shop.nijisanji.jp/s/niji/item/detail/SSZS-27480?ima=0229")
#【バレンタイングッズ2024】アクリルスタンド 狂蘭 メロコ                         
buy1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[7]/div[2]/div[2]/div/button')))
buy1.click()
#【バレンタイングッズ2024】アクリルスタンド 来栖夏芽
buy2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[3]/div[2]/div[2]/div[2]/button')))
buy2.click()
for i in range(4):                                                                  
    add1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[7]/div[2]/div[2]/div/div/button[2]')))
    add1.click()
    add2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[3]/div[2]/div[2]/div[2]/div/button[2]')))
    add2.click()                                                                                 
time.sleep(1)                                                                
#【バレンタイングッズ2024】ランダム缶バッジ
driver.get("https://shop.nijisanji.jp/s/niji/item/detail/SSZS-27479?ima=1737")
buy1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li/div[2]/div[2]/div[2]/button')))
buy1.click()
for i in range(4):
    add1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li/div[2]/div[2]/div[2]/div/button[2]')))
    add1.click()
#【バレンタイングッズ2024】アクリルキーホルダー
time.sleep(1)
driver.get("https://shop.nijisanji.jp/s/niji/item/detail/SSZS-27471?ima=1737")
#【バレンタイングッズ2024】アクリルキーホルダー 狂蘭 メロコ
buy1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[7]/div[2]/div[2]/div/button')))
buy1.click()
#【バレンタイングッズ2024】アクリルキーホルダー 来栖夏芽
buy2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[3]/div[2]/div[2]/div[2]/button')))
buy2.click()
for i in range(4):
    add1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[7]/div[2]/div[2]/div/div/button[2]')))
    add1.click()
    add2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[3]/div[2]/div[2]/div[2]/div/button[2]')))
    add2.click()                                                          
time.sleep(1)
#【バレンタイングッズ2024】長方形クッション
driver.get("https://shop.nijisanji.jp/s/niji/item/detail/SSZS-27463?ima=1737")
#【バレンタイングッズ2024】長方形クッション 狂蘭 メロコ
buy1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[7]/div[2]/div[2]/div/button')))
buy1.click()
#【バレンタイングッズ2024】長方形クッション 来栖夏芽
buy2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[3]/div[2]/div[2]/div[2]/button')))
buy2.click()

for i in range(4):
    add1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[7]/div[2]/div[2]/div/div/button[2]')))
    add1.click()
    add2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VUE_APP_ROOT"]/div/div/main/div/div/div/div[2]/div/div[5]/ul/li[3]/div[2]/div[2]/div[2]/div/button[2]')))
    add2.click()
time.sleep(1)
storecar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="VUE_APP_ROOT"]/div/div/header/div[1]/div/nav/div[1]/form[2]/button')))
storecar.click()