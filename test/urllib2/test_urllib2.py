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
response2 = urllib.request.urlopen(url)
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

