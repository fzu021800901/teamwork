#爬取慢慢买商品列表和价格趋势url

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#showzk > div.zktitle

def get_good(name):
    try:
        driver = webdriver.Chrome()

        # 1、往京东主页发送请求
        driver.get('http://www.manmanbuy.com/')

        # 2、输入商品名称，并回车搜索
        input_tag = driver.find_element_by_id('skey')
        input_tag.send_keys(name)
        input_tag.send_keys(Keys.ENTER)

        goodList = []
        # listpro > div > div > div.bjlineSmall.singlebj.bj_1624812658
        # 通过JS控制滚轮滑动获取所有商品信息
        js_code = '''
             window.scrollTo(0,5000);
         '''
        driver.execute_script(js_code)  # 执行js代码

        # 等待数据加载


        # 3、查找所有商品div
        # good_div = driver.find_element_by_id('J_goodsList')
        good_list = driver.find_elements_by_class_name('bjlineSmall')
        n = 1
        print(type(good_list))
        for good in good_list:
            # 根据属性选择器查找
            # 商品链接
            leftFlag = 0
            rightFlag = 0
            if good.find_element_by_css_selector('.m img').get_attribute('alt') != "京东商城的报价" :
                continue
            good_url = good.find_element_by_css_selector(
                '.t a').get_attribute('href')
            # 商品名称
            good_name = good.find_element_by_css_selector(
                '.t a').get_attribute('onclick')
            '''good_name = good.find_element_by_css_selector(
                '.zktitle').text'''
            start = good_name.find("uploadEvent")
            for index in range(start,len(good_name)):
                if good_name[index] == "'" and leftFlag == 0:
                    leftFlag = index
                    continue
                if good_name[index] == "'":
                    rightFlag = index
                    good_name = good_name[leftFlag+1:rightFlag]
                    break
            # 商品价格
            good_price = good.find_element_by_css_selector(
                '.listpricespan').text.replace("\n", ":")
            # 评价人数
            '''good_commit = good.find_element_by_class_name(
                'p-commit').text1.py.replace("\n", " ")'''

            good_content = {
                             "商品链接": good_url,
                             "商品名称": good_name,
                             "商品价格": good_price }
            goodList.append(good_content)
        time.sleep(2)
        return goodList

    finally:
        driver.close()


if __name__ == '__main__':
    name = "耳机"
    good_list = get_good(name)
    print(good_list)
