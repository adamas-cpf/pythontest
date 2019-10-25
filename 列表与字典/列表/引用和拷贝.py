print('='*25,'X被Y和Z引用','='*25)
X=[1,2,3]
Y=['a',X,'b']
Z={'x':X,'y':2}
print('X--->',X)
print('Y--->',Y)
print('Z--->',Z)

print('='*25,'修改X的值后，Y与Z也会相应改变','='*25)
X[1]='suprise'
print('X--->',X)
print('Y--->',Y)
print('Z--->',Z)

print('='*25,'不使用X.copy()来拷贝','='*25)
A=['welcome','to','cisco']
AA=A
AA[1]='haha'
print('A--->',A)
print('AA--->',AA)

print('='*25,'使用X.copy()来拷贝','='*25)
B=['welcome','to','cisco']
BB=B.copy()
BB[1]='haha'
print('B--->',B)
print('BB--->',BB)
