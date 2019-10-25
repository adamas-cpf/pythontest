print('='*25,'第一种方法','='*25)
A={'qytang':1,'python':2,'cisco':3}
for key in A:
    print(key,'\t',A[key])

print('='*25,'第二种方法--推荐使用','='*25)
B={'qytang':1,'python':2,'cisco':3}
print('='*25,'打印B.item','='*25)
print(B.items())
print('='*25,'遍历打印','='*25)
for Key,Value in  B.items():
    print(Key,'\t',Value)