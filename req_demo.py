# -*- encoding: utf-8 -*-

import requests
# HTTP 请求


# file:///E:/sinhj/readme.txt

# 基本的 get 请求
response = requests.get("https://github.com/")
print(response.status_code)     # 打印状态码
print(response.url)             # 打印请求 url
print(response.headers)         # 打印头信息
print(response.cookies)         # 打印 cookie 信息

# 以文本形式打印网页源码
f_w = open("page_src_text.html", 'w')
f_w.write(response.text.encode("utf-8"))
f_w.close

# 以字节流形式打印
f_w = open("page_src_content.html", 'w')
f_w.write(response.content.decode("utf-8").encode("utf-8"))
f_w.close



# 带参数的 GET 请求

# 直接将参数放在 url 内
response = requests.get(http://httpbin.org/get?name=gemey&age=22)
print(response.text)

# 将参数填写在 dict 中，发起请求时 params 参数指定为 dict
data = {
    'name': 'tom',
    'age': 20
}

response = requests.get('http://httpbin.org/get', params=data)
print(response.text)

# response.json() =? response.text.json()


# Nico
Nico = "https://wx2.sinaimg.cn/large/7db87ea1ly1g5uyya9gklj229a3404qr.jpg"
rsp = requests.get(Nico)
binary_flow = rsp.content
img = Nico.split('/')[-1]
with open(img, 'wb') as f_wb:
    f_wb.write(binary_flow)

Nico = "https://wx1.sinaimg.cn/large/7db87ea1ly1g68r3xccpsj229a3404qr.jpg"
rsp = requests.get(Nico)
binary_flow = rsp.content
img = Nico.split('/')[-1]
with open(img, 'wb') as f_wb:
    f_wb.write(binary_flow)

requests.get('http://httpbin.org/get')
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
requests.options('http://httpbin.org/get')




# 添加头信息
heads = {}
heads['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
response = requests.get('http://www.baidu.com', headers=headers)




# https://www.cnblogs.com/mzc1997/p/7813801.html
# https://www.cnblogs.com/zhaof/p/6915127.html
# https://www.cnblogs.com/lei0213/p/6957508.html

# https://blog.csdn.net/BmwGaara/article/details/79716328

# https://www.cnblogs.com/cmai/p/7967847.html
# https://www.cnblogs.com/woaixuexi9999/p/9404745.html

