#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.parse

class HtmlOutput(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, datas):
        if datas is None:
            return

        for data in datas:
            if data in self.datas:
                continue
            self.datas.append(data)

    def output_html(self):
        if len(self.datas) == 0:
            return

        output_file = open('C:\\Users\\zhangyang\\Desktop\\spider.html', 'w')
        output_file.write('<html>')
        output_file.write('<body>')
        output_file.write('<div>获取连接总数：%d</div>' % len(self.datas))
        output_file.write('<table border=1>')
        output_file.write('<tr>')
        output_file.write('<td>title</td>')
        output_file.write('<td>url</td>')
        output_file.write('</tr>')

        for data in self.datas:
            output_file.write('<tr>\n')
            output_file.write('<td> <a href=%s>%s</a> </td>' % (data['url'], data['title']))
            output_file.write('<td>%s</td>' % urllib.parse.unquote(data['url']))
            output_file.write("</tr>")

        output_file.write('</table>')
        output_file.write('</body>')
        output_file.write('</html>')

        output_file.close()
