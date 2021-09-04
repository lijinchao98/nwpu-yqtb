#-*- coding: UTF-8 -*- 
#from selenium import webdriver
#import selenium
 
#if __name__ == "__main__":
 #   driver = webdriver.Chrome()
 #   driver.get('https://www.baidu.com/')

import time
# 本地Chrome浏览器的静默模式设置：
from selenium import  webdriver #从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行

driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver.get('https://uis.nwpu.edu.cn/cas/login?service=https%3A%2F%2Fecampus.nwpu.edu.cn%2Fc%2Fportal%2Flogin%3Fredirect%3D%252Fweb%252Fguest%252Findex%26p_l_id%3D10213') # 打开翱翔门户登录网页
time.sleep(1)

username = driver.find_element_by_id('username')
username.clear()
username.send_keys('  ')#输入学号
password = driver.find_element_by_id('password')
password.clear()
password.send_keys('  ')#输入密码
time.sleep(1)
driver.find_element_by_name('submit').click()#找到登录按钮并点击按钮
time.sleep(1)

#现在已经登录翱翔门户界面
driver.get('http://yqtb.nwpu.edu.cn/wx/xg/yz-mobile/index.jsp')
time.sleep(1)
#all_handles = driver.window_handles
#driver.switch_to.window(all_handles[1])#会打开两个页面，这里我们切换到第二个页面操作
driver.find_element_by_class_name('icon-shangbao1').click()#抓取健康登记界面的按钮
#进入提问填报界面
time.sleep(1)
    
driver.find_element_by_class_name('weui-btn_primary').click()#抓取提交按钮
sub2=driver.find_element_by_id('brcn')
driver.execute_script("arguments[0].click();", sub2)#这里要打勾，直接点击会报错，查了几篇文章，这个方法可以用
driver.find_element_by_id('save_div').click()
time.sleep(1)
driver.quit()#关闭浏览器
print('1')