import re
#  \d 代表任意一个数字，0-9中任意一个
#  \w 代表任意一个字母或数字或下划线，也就是A~Z，a~z，0~9，_中的任意一个
#  \s 包括空格、制表符、换页符、等空白字符的任意一个
# .  小数点可以匹配除了换行符（\n）以外的任意一个字符

print('='*60)
print(re.match('\d\d\d','123'))
print('='*60)
print(re.match('\d\d\d','12a'))
print('='*60)
print(re.match('\d\d\w','12a'))
print('='*60)
print(re.match('\s',' '))
print('='*60)
print(re.match('\s','   '))
print('='*60)
print(re.match('\s','\n'))
print('='*60)
print(re.match('\s','\r'))
print('='*60)