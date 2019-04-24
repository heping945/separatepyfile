__author__ = 'pinge'


import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 文件目录，复制目录
file_path = BASE_DIR+'\\Python-100-Days\\'
load_path = BASE_DIR+'\\floder\\'

file = os.listdir(file_path)

def run(folder,dst):
	for fchild in os.listdir(folder):
		sChildPath = os.path.join(folder,fchild)
		if os.path.isdir(sChildPath):
			run(sChildPath,dst)
		else:
			# print(sChildPath)
			# if sChildPath.rsplit('.', 1)[-1] == 'md':
			if sChildPath.endswith('.md'):
				shutil.copy(sChildPath,dst)


if __name__ == '__main__':
	run(file_path,load_path)


