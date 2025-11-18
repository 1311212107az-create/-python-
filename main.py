from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 替换为你的评教系统URL
url = " "
# 替换为你的用户名和密码
phone = "your_phone"
pwd = "your_password"

# 替换为ChromeDriver的路径
driver = webdriver.Chrome(executable_path="path/to/chromedriver")

# 登录到评教系统
driver.get(url)
time.sleep(2)  # 等待页面加载

# 找到用户名和密码输入框并输入信息
username_input = driver.find_element(By.ID, "phone")  # 根据实际页面元素调整
password_input = driver.find_element(By.ID, "pwd")  # 根据实际页面元素调整
username_input.send_keys(phone)
password_input.send_keys(pwd)

# 找到登录按钮并点击
login_button = driver.find_element(By.ID, "loginBtn")
login_button.click()
time.sleep(2)  # 等待登录完成

# 进入评教页面
evaluation_page = driver.find_element(By.LINK_TEXT, "评教")  # 根据实际页面元素调整
evaluation_page.click()
time.sleep(2)  # 等待评教页面加载

# 循环处理每一门课程的评价
while True:
    try:
        # 假设每个课程的评分是通过选择下拉菜单完成
        # 找到第一个未评分的课程的下拉菜单
        rating_dropdown = driver.find_element(By.XPATH, "//select[@class='rating-dropdown']")  # 根据实际页面元素调整
        rating_dropdown.click()

        # 输入一个评分值（例如5）
        option_to_select = driver.find_element(By.XPATH, "//option[@value='5']")  # 根据实际页面元素调整
        option_to_select.click()

        # 找到提交按钮并点击
        submit_button = driver.find_element(By.XPATH, "//button[@class='submit-button']")  # 根据实际页面元素调整
        submit_button.click()

        # 等待一段时间，直到系统处理完成
        time.sleep(2)

        # 点击“下一个”按钮
        next_button = driver.find_element(By.XPATH, "//button[@class='next-button']")  # 根据实际页面元素调整
        next_button.click()
        time.sleep(2)
    except:
        print("所有课程评价完成")
        break

# 关闭浏览器
driver.quit()
