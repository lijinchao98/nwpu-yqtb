# !/usr/bin/env python
# -*- coding=UTF-8 -*-
# 阿里云上测试webdriver代码
import time
from selenium import webdriver
def test():
    chromeOptions = webdriver.ChromeOptions()

    chromeOptions.add_argument('--headless')  # 浏览器无窗口加载
    chromeOptions.add_argument('--disable-gpu')  # 不开启GPU加速

    """
    解决报错:
    selenium.common.exceptions.WebDriverException: Message: unknown error: Chrome failed to start: exited abnormally
    (unknown error: DevToolsActivePort file doesn't exist)
    """
    chromeOptions.add_argument('--disable-dev-shm-usage')  # 禁止
    chromeOptions.add_argument('--no-sandbox')  # 以根用户打身份运行Chrome，使用-no-sandbox标记重新运行Chrome

    # 其它设置(可选):
    # chromeOptions.add_argument('--hide-scrollbars') # 隐藏滚动条, 应对一些特殊页面
    # chromeOptions.add_argument('blink-settings=imagesEnabled=false') # 不加载图片, 提升速度
    # chromeOptions.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")  #伪装其它版本浏览器,有时可以解决代码在不同环境上的兼容问题,或者爬虫cookie有效性保持一致需要设置此参数

    # 创建driver对象
    # chrome_options=chromeOptions加载设置
    # executable_path="/usr/bin/chromedriver"指定webdriver路径(可选)
    
    driver = webdriver.Chrome(chrome_options=chromeOptions, executable_path="/usr/bin/chromedriver")
    try:
        driver.get("http://www.baidu.com")
        time.sleep(3)
        print(driver.page_source)
    except Exception as e:
        print(e)
    finally:
        driver.quit()

if __name__ == '__main__':
    test()

