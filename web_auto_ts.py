# -*- encoding: utf-8 -*-

from selenium import webdriver
from time import sleep

web_clt = webdriver.Chrome()

web_clt.get("https://www.baidu.com")

# 写入网页源码到文件
f_w = open("page_src.html", 'w')
f_w.write(web_clt.page_source.encode("utf-8"))
f_w.close



element = web_clt.find_element_by_id("kw")
element.send_keys(u"我可去")

web_clt.find_element_by_id("su").click()

sleep(3)



web_clt.get("https://www.sogou.com/")

web_clt.find_element_by_id("pic").click()

web_clt.find_element_by_id("stswitcher").click()

upload = web_clt.find_element_by_id("upload_pic_file")
upload.send_keys(ur"D:\花媛\陳絲旋\3276050.jpg")  # send_keys

sleep(3)

web_clt.close()



# 如何判定是否成功
