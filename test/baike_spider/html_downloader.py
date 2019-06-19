#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import http.cookiejar
import urllib.request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)
        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()
