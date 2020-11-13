import text1,text2,text3

if __name__ == '__main__':
    name = ["速溶咖啡","麦片","成人奶粉","纯牛奶","酸奶","豆奶","巧克力","坚果","面包","豆干","蜜饯","薯片","饼干"]  #输入要爬取的名称
    for index in range(len(name)):
        good_list = text3.get_good(name[index])

        for index1 in range(len(good_list)):
            text2.mmm(good_list[index1]["商品链接"],name[index])


