# IDE: PyCharm
# time: 2023/4/15 1:00
# file: : test.py
# author: Sakura
# Description:
import fitz
import os
source_folder=r'D:\Browser\院毅电力拖动自动控制系统第五版答案_-_哔哩哔哩\DM_20230412134233_001.WEBP'
# source_folder = source_folder.replace('\\', '/')
# source_folder = source_folder + "" if source_folder.endswith("/") else source_folder + "/"
# print(source_folder)
# included_extensions = ['jpg', 'jpeg', 'png', 'webp']
# included_extensions += [i.upper() for i in included_extensions]
# print(included_extensions)
# file_names = [fn for fn in os.listdir(source_folder)
#               if any(fn.endswith(ext) for ext in included_extensions)]
# print(file_names)
fitz.open(source_folder)
