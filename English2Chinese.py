# coding: utf-8
import requests
from bs4 import BeautifulSoup

# 获取源文件
path = '/home/origami/Desktop/e2c.html'
with open(path, 'r', encoding='utf-8') as prefab_list_text:
    soup = BeautifulSoup(prefab_list_text.read(-1), 'html5lib')

chinese_dict = {}
for t in soup.select('#mw-content-text > table')[1:]:
    for tr in t.tbody.contents[2::2]:
        # print('%s : %s' % (tr.contents[1].text[:-1], tr.contents[2].text[:-1]))
        chinese_dict[tr.contents[1].text[:-1]] = tr.contents[2].text[:-1]

