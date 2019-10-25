print('='*25,'列表的插入','='*25)
# L.insert(index,'object')在index序列号前插入object对象
L=['Welcome','to','trcbank']
L.insert(1,'haha')
print(L)

print('='*25,'列表的删除','='*25)
A=['Welcome','to','trcbank']
A.remove('to')
print(A)

print('='*25,'列表的弹出','='*25)
# 列表的弹出的是最后一位元素，并且弹出是有返回值的，这个可以在CMD下的互动界面尝试是否有返回值
BB=['Welcome','to','trcbank']
BB.pop()
print(BB)

print('='*25,'查看列表的弹出后返回结果','='*25)
B=['Welcome','to','trcbank']
C=B.pop()
print(C)

print('='*25,'列表append和extend的区别','='*25)
D=[1,2,3,4]
E=[5,6,7,8]
print('='*25,'append结果','='*25)
# 注意此处使用print(D.append[E])的方式会报错只能使用以下方式
D.append(E)
print(D)

print('='*25,'extend结果','='*25)
#extend相当于F+G
F=[1,2,3,4]
G=[5,6,7,8]
F.extend(G)
print(F)

print('='*25,'查找列表某元素的位置','='*25)
H=[1,2,3,4,5,5,6,7,7]
print(H.index(5))

print('='*25,'计算列表中某元素出现的次数','='*25)
print(H.count(7))

print('='*25,'正向排序','='*25)
J=[1,34,2,435,5,32,8]
J.sort()
print(J)

print('='*25,'反向排序','='*25)
#注意reverse是反转并不是反向排序，例如[1,5,3,4]使用reverse后变成的是[4,3,5,1]
K=[1,34,5,6,99,45]
K.sort()
K.reverse()
print(K)

