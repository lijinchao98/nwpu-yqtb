#-*- coding: UTF-8 -*- 
import time
# 本地Chrome浏览器的静默模式设置：
from selenium import  webdriver #从selenium库中调用webdriver模块

def yqtb_nwpu():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--no-sandbox')#让Chrome在root权限下跑
    chromeOptions.add_argument('--disable-dev-shm-usage')
    chromeOptions.add_argument('---disable-gpu')
    chromeOptions.add_argument('--headless') # 把Chrome浏览器设置为静默模式
    driver = webdriver.Chrome(chrome_options = chromeOptions, executable_path="/usr/bin/chromedriver") #
    driver.get('https://uis.nwpu.edu.cn/cas/login?service=https%3A%2F%2Fecampus.nwpu.edu.cn%2Fc%2Fportal%2Flogin%3Fredirect%3D%252Fweb%252Fguest%252Findex%26p_l_id%3D10213') # 打开翱翔门户登录网页
    time.sleep(1)

    username = driver.find_element_by_id('username')
    username.clear()
    username.send_keys('*********')#输入学号
    password = driver.find_element_by_id('password')
    password.clear()
    password.send_keys('*********')#输入密码
    time.sleep(1)
    driver.find_element_by_name('submit').click()#找到登录按钮并点击按钮
    time.sleep(1)

    #现在已经登录翱翔门户界面
    driver.get('http://yqtb.nwpu.edu.cn/wx/xg/yz-mobile/index.jsp')#获取体温填报的链接(没找到element，我直接打开链接网站)
    time.sleep(1)
    driver.find_element_by_class_name('icon-shangbao1').click()#抓取健康登记界面的按钮
    #进入提问填报界面
    time.sleep(1)
    
    #2021年底西安疫情，每天核酸，填报系统多了一个选项，需要加上这个，点击“已检测”
    a = driver.find_element_by_xpath("/html/body/div[@class='page']/form/div[@id='rbxx_div']/div[3]/label[2]/div[2]/input")
    driver.execute_script("arguments[0].click();", a)
    time.sleep(1)
    
    driver.find_element_by_class_name('weui-btn_primary').click()#抓取提交按钮
    sub2=driver.find_element_by_id('brcn')
    driver.execute_script("arguments[0].click();", sub2)#这里要打勾，直接点击会报错，查了几篇文章，这个方法可以用
    driver.find_element_by_id('save_div').click()
    time.sleep(1)
    driver.quit()#关闭浏览器
