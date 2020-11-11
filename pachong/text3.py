
#爬取京东商品信息，包括商品url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



def get_good(driver):
    try:
        good_list = []
        # listpro > div > div > div.bjlineSmall.singlebj.bj_1624812658
        # 通过JS控制滚轮滑动获取所有商品信息
        js_code = '''
             window.scrollTo(0,5000);
         '''
        driver.execute_script(js_code)  # 执行js代码

        # 等待数据加载
        time.sleep(2)

        # 3、查找所有商品div
        # good_div = driver.find_element_by_id('J_goodsList')
        good_list = driver.find_elements_by_class_name('bjlineSmall')
        n = 1
        for good in good_list:
            # 根据属性选择器查找
            # 商品链接
            leftFlag = 0
            rightFlag = 0

            good_url = good.find_element_by_css_selector(
                '.poptrend a').get_attribute('href')

            # 商品名称
            good_name = good.find_element_by_css_selector(
                '.t a').get_attribute('onclick')
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
                             "价格趋势链接": good_url,
                             "商品名称": good_name,
                             "商品价格": good_price }
            good_list.append(good_content)
            print(good_content)


        time.sleep(2)
        return good_list

    finally:
        driver.close()


if __name__ == '__main__':
    good_name = input('请输入爬取商品信息:').strip()

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # 1、往京东主页发送请求
    driver.get('http://www.manmanbuy.com/')

    # 2、输入商品名称，并回车搜索
    input_tag = driver.find_element_by_id('skey')
    input_tag.send_keys(good_name)
    input_tag.send_keys(Keys.ENTER)
    time.sleep(2)

    good_list = get_good(driver)
    print(good_list)
