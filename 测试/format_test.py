dep1 = 'Security'
dep2 = 'Python'
name1 = 'caipf'
name2 = 'adamas'
money1 = 34234.34234
money2 = 45464.562
line1 = 'Department name:{0:<10}Manager:{1:<10}Course Fees:{2:<10.2f}'.format(dep1,name1,money1)
line2 = 'Department name:{0:<10}Manager:{1:<10}Course Fees:{2:<10.2f}'.format(dep2,name2,money2)
# line1 = 'Department name:%-10sManager:%-10sCourse Fees:%-10.2f'%(dep1,name1,money1)
# line2 = 'Department name:%-10sManager:%-10sCourse Fees:%-10.2f'%(dep2,name2,money2)
length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)