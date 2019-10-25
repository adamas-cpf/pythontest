import re
str='0005-330a-a9a4   1          Learned          GE1/2/0/14 '
newstr=re.match('\s*(\w*-?\w*-?\w*)\s+(\d*)\s+(\w*)\s+(\w*\d*/\d*/\d*/\d*)',str)
print('{0:<15}\t:{1:<10}'.format('MAC',newstr[1]))
print('{0:<15}\t:{1:<10}'.format('Vlan ID',newstr[2]))
print('{0:<15}\t:{1:<10}'.format('State',newstr[3]))
print('{0:<15}\t:{1:<10}'.format('interface',newstr[4]))