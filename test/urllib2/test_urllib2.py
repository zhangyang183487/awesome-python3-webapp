#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import http.cookiejar
import urllib.request

url = "https://www.baidu.com"

print("第一种请求方式")
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(response1.read())

print("第二种请求方式")
request = urllib.request.Request(url)
request.add_header("User-Agent", "Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(response2.read())

print("第三种请求方式")
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(response3.read())
print(cj)

print("第四种请求方式")
cj2 = http.cookiejar.CookieJar()
opener2 = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj2))
response4 = opener2.open(url)
print(response4.code)
print(response4.read())
print(cj2)
print("\n")
for item in cj:
    print(item.name + '=' + item.value)

print("代理请求方式")
proxy_handler = urllib.request.ProxyHandler({
    # 代理服务器IP地址
    'http': 'http://172.21.25.20:8080',
    'https': 'https://172.21.25.20:8080'
})
opener3 = urllib.request.build_opener(proxy_handler)
response5 = opener3.open(url)
# 获取状态码，如果是200表示成功
print(response5.status)
# 读取网页内容
print(response5.read().decode('utf-8'))
