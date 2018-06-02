from Prefab2English import prefab_dict
from English2Chinese import chinese_dict

# UI
while True:
    print('Entry prefab\'s name:', end='')
    pname = input()
    if pname == 'exit':
        break

    en_name = ''
    for (type_name, table) in prefab_dict.items():
        if pname in table:
            en_name = table[pname]

    zh_name = ''
    if en_name in chinese_dict:
        zh_name = chinese_dict[en_name]

    print('The English and Chinese name of "%s" is: "%s"  "%s"' % (pname, en_name, zh_name))