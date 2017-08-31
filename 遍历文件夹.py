# -*- coding:utf-8 -*-
import os
""" 遍历文件夹内的每个文件
   os.walk """
文件夹 = input("请输入文件夹路径：")
for 父文件夹,文件夹,文件列表 in os.walk(文件夹):
    for 文件名 in 文件列表:
        文件路径 = os.path.join(父文件夹, 文件名)
        print(文件路径)
