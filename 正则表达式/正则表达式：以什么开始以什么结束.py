import re
#   ^   与字符开始的地方匹配，不匹配任何字符
#   $   与字符结束的地方匹配，不匹配任何字符
#   \b  匹配一个单词边界，也就是单词和空格中间的位置，匹配任何字符
print('='*60)
print(re.match('^qytang','qytang'))
print('='*60)
print(re.match('^ccies','qytangccies'))
print('='*60)
print(re.match('.*ccies$','qytangccies'))
print('='*60)
