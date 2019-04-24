__author__ = 'pinge'

# 添加上级文件夹路径
import sys
sys.path.append('..')
print(sys.path)

path = 'utils.cors.Xxx'

import importlib

module_path,class_name = path.rsplit('.', maxsplit=1)
print(module_path)
 # 根据字符串的形式导入模块
m = importlib.import_module(module_path)
cls = getattr(m, class_name)
print(cls)

cls().pp()


