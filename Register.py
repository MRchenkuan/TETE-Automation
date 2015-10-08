# coding=utf-8
from selenium import webdriver
import time
from Tools.Data.PhoneNumForReg import Numbers
from selenium.webdriver.support.ui import Select
import unittest,os,time,re
import MySQLdb
from CreateShop import CreateShop
from ShopLogin import ShopLogin

'''
    此处为前台注册的基本类
'''
class AcctRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        print self.driver.title
        self.verificationErrors = []
        # self.accept_next_alert = True

    def test_01_register(self):
        #手机号
        for phonenumb in Numbers:
            driver = self.driver
            driver.get("http://tete.haodou.com/admin/user/register.php")
            reg_phone = driver.find_element_by_id('reg_phone')
            reg_captcha = driver.find_element_by_id('reg_captcha')
            btn_captcha = driver.find_element_by_id('btn_captcha')
            reg_checkbox = driver.find_element_by_id('reg_checkbox')
            reg_pass = driver.find_element_by_id('reg_pass')
            btn_reg = driver.find_element_by_id('btn_reg')

            #填写手机号，并获取验证码
            reg_phone.send_keys(phonenumb)
            btn_captcha.click()
            PhoneNumResult = driver.find_element_by_xpath("//input[@id='reg_phone']/preceding-sibling::p").text

            if PhoneNumResult != u'该手机号已经被注册':
                #根据手机号查验证码
                conn = MySQLdb.connect(host="192.168.1.135", user="proxy_r", passwd="proxy",charset='utf8')
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM tete_admin.SmsLog a WHERE a.Mobile =%s"%phonenumb)
                captcha = cursor.fetchall()[-1][4]

                #填写余下信息
                reg_captcha.send_keys(captcha)
                reg_pass.send_keys('123456')
                reg_checkbox.click()

                #提交注册
                btn_reg.click()
                time.sleep(3)
                CreateShop(self.driver)
            else:
                #已经注册那么转入登录流程
                print u'SELENIUM:已经注册，准备转入登录流程！'
                ShopLogin(driver,phonenumb,'123456')
                CreateShop(self.driver)
            time.sleep(1.5)
            driver.find_element_by_link_text(u'退出登录').click()
            time.sleep(1.5)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    print 'ok'