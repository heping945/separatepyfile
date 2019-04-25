# 数组查找
class Solution:
	'''input:[1,2,3,4,5],target=9,out:[3,4]'''
	def slist(self,nums,target):
		hashmap = {}
		for index,num in enumerate(nums):
			another_num = target-num
			if another_num in hashmap:
				return [hashmap[another_num],index]
			hashmap[num] = index
s = Solution()
r=s.slist([1,2,3,4,5],9)
print(r)

# 单例模式
class Singe:
	def __new__(cls,*args,**kwargs):
		if not hasattr(cls, '_instance'):
			_instance = super().__new__(cls,*args,**kwargs)
			cls._instance = _instance
		return cls._instance

a = Singe()
b = Singe()
print(a is b)

# 装饰器
from functools import wraps
import time
def timelog(_int=False):
	def log(func):
		@wraps(func)
		def _log(*args,**kwargs):
			beg = time.time()
			res = func(*args,**kwargs)
			if _int:
				print('耗时：%s s'%(int(time.time()-beg)))
			else:
				print('耗时：%s s'%(time.time()-beg))
			return res
		return _log
	return log
@timelog(True)
def mytime():
	time.sleep(1)
mytime()

class TimeLog:
	def __init__(self,_int=False):
		self._int = _int
	def __call__(self,func):
		@wraps(func)
		def _log(*args,**kwargs):
			beg = time.time()
			res = func(*args,**kwargs)
			if self._int:
				print('耗时：%s s'%(int(time.time()-beg)))
			else:
				print('耗时：%s s'%(time.time()-beg))
			return res
		return _log

@TimeLog(True)
def mtime():
	time.sleep(1)
mtime()

