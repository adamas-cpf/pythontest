import re
#\r,\n代表回车和换行符
#\t代表制表符
#\\代表"\"本身
#\^匹配^符号本身
#\$匹配$符号本身
#\.匹配小数点（.）本身
print('='*60)
print(re.match('cmd.exe','cmdaexe'))
print('='*60)
print(re.match('cmd.exe','cmdbexe'))
print('='*60)
print(re.match('cmd.exe','cmd.exe'))
print('='*60)
print(re.match('cmd\.exe','cmd.exe'))
print('='*60)
print(re.match('cmd\.exe','cmdaexe'))
print('='*60)