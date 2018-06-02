# coding: utf-8
import requests
from bs4 import BeautifulSoup

# prefab_list_web = requests.get('http://dontstarve.wikia.com/wiki/Console/Prefab_List')
# 获取源文件
path = '/home/origami/Desktop/prefab_list.html'
with open(path, 'r', encoding='utf-8') as prefab_list_text:
    soup = BeautifulSoup(prefab_list_text.read(-1), 'html5lib')

# 最终输出, 格式为{'prefab类型': {'prefab名': '英文名'}}
prefab_dict = {}
# 对于主内容下的每一个表和每个表前的h2(第一个不是表示表的h2)
for t, h in zip(soup.select('#mw-content-text > table'), soup.select('#mw-content-text > h2')[1:]):
    # 标题为当前表前的h2标题中的第一个span标签
    tab_name = h.span.text
    # 遍历tr, 取第二个td(prefab名)为key, 第一个(English名)为value
    # 由于某些不可预知的bug, 每一个tbody下的tr标签都隔一个才是有效的, 其他都是空的, 故取2::2
    tab = {}
    for tr in t.tbody.contents[2::2]:
        # [:-1]去掉\n
        tab[tr.contents[2].text[:-1]] = tr.contents[1].text[:-1]
    # 最后以h2为key, 上表为value插入输出
    prefab_dict[tab_name] = tab


