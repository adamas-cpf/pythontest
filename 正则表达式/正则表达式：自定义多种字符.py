import re
#   [ab5@]  匹配"a"或"b"或"5"或"@"
#   [^abc]  匹配"a","b","c"之外的任意一个字符
#   [f-k]   匹配"f"-"k"之间的任意一个字母
#   [^A-F0-3]   匹配"A"-"F",0-3之外的任意一个字符

print('='*60)
print(re.match('a[a-z]c','abc'))
print('='*60)
print(re.match('a[a-z]c','a1c'))
print('='*60)
print(re.match('a[0-9]c','a1c'))
print('='*60)
print(re.match('a[^a-z]c','a2c'))
print('='*60)