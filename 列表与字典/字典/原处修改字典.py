print('='*25,'修改键值,将qytang键值修改','='*25)
A={'qytang':1,'python':2,'cisco':3}
A['qytang']=['beijing','shanghai','tianjin','chongqing']
print(A)

print('='*25,'删除cisco键值','='*25)
B={'qytang':1,'python':2,'cisco':3}
del B['cisco']
print(B)

print('='*25,'如果键值存在就原处修改，如果不存在就添加新键值','='*25)
C={'qytang':1,'python':2,'cisco':3}
C['adamas']=4
print(C)

