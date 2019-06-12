# -*- coding: utf-8 -*
'''
遍历文件夹中的文件
'''

import os
dir = r"D:\张慕明\2018产业杰出人物\产业杰出人物在2019产业大会的宣传资料\挑选出来的照片"
dirs = os.listdir(dir)
for dirc in dirs:
    print(dirc)
'''
print(dirs)
print(len(dirs))
'''
#python D:\Github\customs_vegetable_data\遍历文件夹中的文件.py
