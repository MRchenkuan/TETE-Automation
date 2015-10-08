# coding=utf-8

import time
from Tools import Data
import os
'''
    商铺创建
'''
def CreateShop(driver):
    driver.get('http://tete.haodou.com/admin/user/shop.php?do=add')
    if driver.title != u'特特商家后台商品审核':
        shop_name = driver.find_element_by_id('shop_name')
        shop_address = driver.find_element_by_id('shop_address')
        shop_mobile = driver.find_element_by_id('shop_mobile')

        #图像
        shop_avatar = driver.find_element_by_id('shop_avatar')

        shop_desc = driver.find_element_by_id('shop_desc')#简介
        user_name = driver.find_element_by_id('user_name')#联系人

        shop_licence = driver.find_element_by_id('shop_licence')#营业执照
        user_card = driver.find_element_by_id('user_card')#身份证

        user_id_num = driver.find_element_by_id('user_id_num')#身份证号码
        money_account = driver.find_element_by_id('money_account')#收款帐号
        money_bank = driver.find_element_by_id('money_bank')#银行类型
        money_name = driver.find_element_by_id('money_name')#开户名

        btn_shop_add = driver.find_element_by_id('btn_shop_add')#添加按钮


        shop_name.send_keys((u'shop%s'%time.time())[0:14])
        shop_address.send_keys(u'Automation湖南长沙xxx地方')

        imgsrc = os.sep.join(os.getcwd().replace('\\','/').split('/')+['Tools','Data','000.jpg'])

        shop_avatar.send_keys(imgsrc)
        time.sleep(1)
        shop_mobile.send_keys('13874900776')
        shop_desc.send_keys(u'这里是%s的店铺介绍，这是脚本自动生成的一个店铺，生成时间为%s，以做内部测试之用。'%(shop_name.get_attribute('value'),time.time()))

        user_name.send_keys(u'自动化程序')
        shop_licence.send_keys(imgsrc)
        time.sleep(1)
        user_card.send_keys(imgsrc)
        time.sleep(1)
        user_id_num.send_keys((u'40000000%s'%time.time())[0:18])

        money_account.send_keys('6222222222222222222')
        money_name.send_keys(u'自动化程序')
        #添加
        btn_shop_add.click()
    else:
        print u'该商家已开店'
