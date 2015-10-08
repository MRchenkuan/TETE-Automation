# coding=utf-8
import time
from Tools.getCapture import getCapture

def ShopLogin(driver,phone,psw):
    driver.get('http://tete.haodou.com/admin/user/login.php')
    login_phone = driver.find_element_by_id('login_phone')
    login_password = driver.find_element_by_id('login_password')
    login_captcha = driver.find_element_by_id('login_captcha')

    login_phone.send_keys(phone)
    login_password.send_keys(psw)
    login_captcha.send_keys(getCapture(type='sj',ssid=driver.get_cookie('YCSSID').get('value')))

    btn_login = driver.find_element_by_id('btn_login')
    btn_login.click()
    time.sleep(2)