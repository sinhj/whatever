# -*- encoding: utf-8 -*-

from urllib2 import Request, urlopen



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"}
foo_url = "https://www.baidu.com"
bar_html = urlopen(Request(foo_url, headers=headers)).read()

with open("rst.html", 'w') as f_w:
    f_w.write(bar_html)
