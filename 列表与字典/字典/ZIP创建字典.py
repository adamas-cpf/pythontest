print('='*25,'使用zip创建字典','='*25)
A=dict(zip(['qytang','python','cisco'],[1,2,3]))
print(A)

print('='*25,'字典解析第一种方法','='*25)
B={b:b**2for b in [1,2,3,4,5]}
print(B)

print('='*25,'字典解析第二种方法','='*25)
C={}
for c in [1,2,3,4,5]:
    C[c]=c**2
print(C)

print('='*25,'针对字符串字典解析第一种方法','='*25)
D={d:d*4for d in 'qytang'}
print(D)

print('='*25,'针对字符串字典解析第二种方法','='*25)
E={}
for e in 'qytang':
    E[e]=e*4
print(E)

print('='*25,'字典解析举例1','='*25)
F={f.upper():f for f in ['qytang','python','cisco']}
print(F)

print('='*25,'字典解析举例2','='*25)
G={}
for g in ['qytang','python','cisco']:
    key=g.upper()
    value=g
    G[key]=value
print(G)

print('='*25,'字典解析举例3','='*25)
H={h:v*3for (h,v) in zip(['qytang','python','cisco'],[1,2,3])}
print(H)

print('='*25,'字典解析举例4','='*25)
I={}
I1={'qytang':1,'python':2,'cisco':3}
for (KEY,VALUE) in I1.items():
    I[KEY]=VALUE*3
print(I)