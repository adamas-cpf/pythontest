import re
str='RAGG101.3001        up       up       20.2.4.185      To_Fw '
newstr=re.match('\s*(\w*\d.\d*)\s+(\w*)\s+(\w*)\s+(\d.*?)\s+(\w*)\s*',str)
print('{0:<20}\t:{1:<10}'.format('接口名称',newstr[1]))
print('{0:<20}\t:{1:<10}'.format('接口物理状态',newstr[2]))
print('{0:<20}\t:{1:<10}'.format('接口协议状态',newstr[3]))
print('{0:<20}\t:{1:<10}'.format('接口IP地址',newstr[4]))
print('{0:<20}\t:{1:<10}'.format('接口所属vrf',newstr[5]))
#中文字符对其时后面要加1个\t
# print('{0:<10} :{1:<10}'.format('interface',newstr[1]))
# print('{0:<10} :{1:<10}'.format('physical',newstr[2]))
# print('{0:<10} :{1:<10}'.format('protocol',newstr[3]))
# print('{0:<10} :{1:<10}'.format('IP',newstr[4]))
# print('{0:<10} :{1:<10}'.format('vrf',newstr[5]))


