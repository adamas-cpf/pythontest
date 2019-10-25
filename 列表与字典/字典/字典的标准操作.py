print('='*25,'第一种创建字典的方法','='*25)
L={'qytang':1,'python':2,'cisco':3}
print(L['qytang'])

print('='*25,'第二种创建字典的方法','='*25)
A=dict(qytang=1,python=2,cisco=3)
print(A)
print(A['qytang'])

print('='*25,'计算字典长度','='*25)
B={'qytang':1,'python':2,'cisco':3}
print(len(B))

print('='*25,'取字典中的键','='*25)
C={'qytang':1,'python':2,'cisco':3}
print(list(C.keys()))

print('='*25,'取字典中的值','='*25)
D={'qytang':1,'python':2,'cisco':3}
print(list(D.values()))