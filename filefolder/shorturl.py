__author__ = 'pinge'

# 10进制转二进制
def mybin(num):
	global res
	res = []
	while num:
		num,x = divmod(num, 2)
		res.append(str(x))
	res.reverse()
	return ''.join(res)
n=mybin(10)
print(n)


# md5的摘要算法
import hashlib
x = hashlib.md5()
x.update('hxashdsad'.encode())
print(x.hexdigest())


# 62进制的短网址转化，根据传入数字转化
CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def encoden(num):
	if num == 0:
		return CHARS[0]
	res = []
	while num:
		num,x = divmod(num, len(CHARS)) #62
		res.append(CHARS[x])
	return ''.join(reversed(res))
# r = encoden(10000000)
r = encoden(5)
print(r)

