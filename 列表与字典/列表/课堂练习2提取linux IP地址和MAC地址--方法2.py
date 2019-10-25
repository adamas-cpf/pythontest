import os
import re
ifconfig_result=os.popen("ifconfig"+' '+"ens33").read()
print(ifconfig_result)
IP=re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)
print(IP)
print('{0:<20}:{1:<10}'.format('IP',IP[0]))
print('{0:<20}:{1:<10}'.format('Mask',IP[1]))
print('{0:<20}:{1:<10}'.format('Boardcast',IP[2]))
MAC=re.findall('(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)',ifconfig_result)
print('{0:<20}:{1:<10}'.format('Mac address',MAC[0]))