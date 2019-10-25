import os
import re
# 提取linux ifconfig ens33的配置
ifconfig_result=os.popen("ifconfig"+' '+'ens33').read()
A=re.split('\n',ifconfig_result)
IP=[]
for x in A:
    #y=x.split()
    for z in x.split():
       if re.match('.*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*',z):
              IP.append(z)
print('{0:<10}:{1:<10}'.format('IP',IP[0]))
print('{0:<10}:{1:<10}'.format('Mask',IP[1]))
print('{0:<10}:{1:<10}'.format('Boardcast',IP[2]))


