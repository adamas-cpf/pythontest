print('='*25,'使用get获取一个存在的键值','='*25)
A={'qytang':1,'python':2,'cisco':3}
print(A.get('qytang'))

print('='*25,'使用get获取一个不存在的键值','='*25)
B={'qytang':1,'python':2,'cisco':3}
print(B.get('haha'))

print('='*25,'使用get获取一个不存在的键值并返回预定义结果','='*25)
D={'qytang':1,'python':2,'cisco':3}
print(B.get('haha',88))


print('='*25,'不使用get获取一个不存在的键值','='*25)
C={'qytang':1,'python':2,'cisco':3}
# 注意此处会报错误，如果用get不存在会返回none并不会报错
print(C['haha'])