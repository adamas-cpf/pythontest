print('='*25,'如果键值存在就原处修改，如果键值不存在就添加新键','='*25)
A={'qytang':1,'python':2,'cisco':3}
B={'cisco':'haha','trcbank':'adamas'}
A.update(B)
print(A)