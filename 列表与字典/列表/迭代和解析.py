print('='*25,'列表for循环操作','='*25)
L=[1,2,3,4]
for x in L:
    print(x,end='')

print('='*25,'列表的高级迭代','='*25)
B=[x*4 for x in 'abc']
print(B)

print('='*25,'列表的简单迭代','='*25)
C=[]
for z in 'abc':
    C.append(z*4)
print(C)