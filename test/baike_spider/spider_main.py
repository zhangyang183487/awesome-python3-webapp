#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutput()

    def craw(self, root_url):
        count = 1  # 当前爬取url

        self.urls.add_new_url(root_url)  # 添加入口url

        # 当有新的url时
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()  # 从urls获取行的url页面
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)  # 下载url页面
                new_urls, new_data = self.parser.parse(html_cont)  # 解析下载页面
                self.urls.add_new_urls(new_urls)  # 添加批量url
                self.outputer.collect_data(new_data)  # 收集新的数据

                if count == 1000:
                    break

                count = count + 1
            except Exception as e:
                print('carw failed--', e)

        # 输出收集好的数据
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
