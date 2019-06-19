#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import urllib.parse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, cont):
        if cont is None:
            return None

        soup = BeautifulSoup(cont, 'html.parser')
        new_urls = self._get_new_urls(soup)
        new_datas = self._get_new_datas(soup)

        return new_urls, new_datas

    def _get_new_urls(self, soup):
        new_urls = set()

        links = soup.find_all('a', href=re.compile(r"/item/*"))
        for link in links:
            url = link['href']
            full_url = urllib.parse.urljoin('https://baike.baidu.com', url)
            new_urls.add(full_url)

        return new_urls

    def _get_new_datas(self, soup):
        new_datas = []
        links = soup.find_all('a', href=re.compile(r"/item/*"))
        for link in links:
            url = link['href']
            title = link.get_text()
            full_url = urllib.parse.urljoin('https://baike.baidu.com', url)
            new_data = {'title': title, 'url': full_url}
            new_datas.append(new_data)

        return new_datas
