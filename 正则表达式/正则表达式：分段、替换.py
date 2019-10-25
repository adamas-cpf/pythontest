import re
print('='*25,'分段','='*25)
print(re.split('---','aaa---bbb---ccc'))
print('='*25,'替换','='*25)
print(re.sub('--','...','aaa--bbb--ccc'))
print('='*25,'用于分段匹配','='*25)
print(re.split('[-=]','aaa-bbb=ccc'))
print('='*25,'分段1','='*25)
str1='abc/def/ghi'
newstr1=str1.split('/')
print(newstr1)
print('='*25,'分段2','='*25)
str2='abc/def/ghi'
newstr2=re.match('(.*)/(.*)/(.*)',str2).groups()
print(newstr2)
print('='*25,'分段3','='*25)
str3='<abc><def><ghi>'
newstr3=re.match('<(.*)><(.*)><(.*)>',str3).groups()
print(newstr3)
print('='*25,'分段4','='*25)
str4='hello haha hehe'
newstr4=re.split(' ',str4)
print(newstr4)
print('='*25,'分段5','='*25)
str5='hellohaha hehe'
newstr5=re.match('hello\s*([a-z]*)\s+(.*)',str5).groups()
print(newstr5)

