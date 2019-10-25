import re
#   |   左右两边表达式之间"或"关系，匹配左边或者右边
#  （） （1）.在被修饰匹配次数的时候，括号中的表达式可以作为整体被修饰
#       （2）.取匹配结果的时候，括号中的表达式匹配到的内容可以单独得到
print('='*60)
print(re.match('root|Root','root'))
print('='*60)
print(re.match('root|Root','Root'))
print('='*60)
print(re.match('[Rr]oot','root'))
print('='*60)
print(re.match('[Rr]oot','Root'))
print('='*60)