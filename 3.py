from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
PHONE = "your phone number"
PWD   = "your password"
EVAL_URL = ("https://newes.chaoxing.com/pj/frontv2/whatIEvaluatedDetails?questionnaireId=xxx，评教系统的url自己写")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

# 1. 登录
driver.get("https://passport2.chaoxing.com/login?fid=&newversion=true&refer=https%3A%2F%2Fi.chaoxing.com")
wait.until(EC.presence_of_element_located((By.ID, "phone"))).send_keys(PHONE)
wait.until(EC.presence_of_element_located((By.ID, "pwd"))).send_keys(PWD)
wait.until(EC.element_to_be_clickable((By.ID, "loginBtn"))).click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img.head-img")))
print("登录成功")

# 2. 跳进评教页面
driver.get(EVAL_URL)
wait.until(EC.url_contains("whatIEvaluatedDetails"))

wait = WebDriverWait(driver, 10)

# 1. 点“评价状态”本身

wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//span[text()='评价状态']")
)).click()
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//li[text()='未评']")
)).click()
print("已切换为“未评”")




while True:
    # 1. 点第一行评价
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//tr[1]//a[contains(text(),'评价') or contains(text(),'去评价')]")
    )).click()

    # 2. 填20 + 提交 + 确定
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "input[type='text'], textarea")))
    for box in driver.find_elements(By.CSS_SELECTOR, "input[type='text'], textarea"):
        if box.is_displayed() and box.is_enabled():
            box.clear()
            box.send_keys("20")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.save"))).click()
    ok_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.layui-layer-btn0")))
    ok_btn.click()

    time.sleep(5)   #

input(">>> 浏览器已保留，按 Enter 才会结束 <<<")
