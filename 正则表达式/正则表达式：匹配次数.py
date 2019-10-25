import re
#   {n}     表达重复n次，比如"\w{2}"相当于"\w\w"；"a{5}"相当于aaaaa
#   {m,n}   表达至少重复m次，最多重复n次，比如"ba{1,3}"可以匹配"ba","baa","baaa"
#   {m,}    表达至少重复m次，比如"\w\d{2,}"可以匹配"a12","_456","M12344"
#    ?      匹配表达式0次或者1次，相当于{0,1}，比如"a[cd]?"可以匹配"a","ac","ad"
#    +      表达式至少出现1次，相当于{1,},比如"a+b"可以匹配"ab","aab","aaab"
#    *      表达式不出现或者出现任意次，相当于{0,},比如"\^*b"可以匹配"b","^^^b"
#
print ('='*60,'重复n次')
print(re.match('a{5}','aaaaa'))
print('='*60,'?匹配表达式0次或者1次')
print(re.match('ba(na)?','ba'))
print('='*60)
print(re.match('ba(na)?','bana'))
print('='*60)
print(re.match('ba(na)?','banana'))
print('='*60,'*表达式不出现或者出现任意次')
print(re.match('ba(na)*','ba'))
print('='*60)
print(re.match('ba(na)*','bana'))
print('='*60)
print(re.match('ba(na)*','banana'))