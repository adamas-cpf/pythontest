import re
print('='*25,'找到出现位置','='*25)
str1='abc/def/ghi'
print(str1.find('def'))
print('='*9,'找到所有匹配所有<(.*?)的内容，然后产生列表>','='*10)
str2='<abc>/<def>/<ghi>'
newstr2=re.findall('<(.*?)>',str2)
print(newstr2)
print('='*25,'str3','='*25)
str3='<abc>/<def>....<ghi>/<jkl>'
newstr3=re.findall('<(.*?)>/?<(.*?)>',str3)
print(newstr3)
print('='*25,'str4:search找到第一个','='*25)
str4='<abc>/<def>....<ghi>/<jkl>'
newstr4=re.search('<(.*?)>/?<(.*?)>',str4).groups()
print(newstr4)
print('='*25,'str5:findall找到所有匹配的','='*25)
str5='<abc>/<def>....<ghi><jkl>'
newstr5=re.findall('<(.*?)>/?<(.*?)>',str5)
print(newstr5)
