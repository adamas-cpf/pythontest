print('='*20,'剥离两边的空白','='*20)
s='\n\twelcome to qytang\n\r\t'
ss=s.strip()
print(ss)
print('='*20,'剥离左边的空白','='*20)
sl=s.lstrip()
print(sl)
print('='*20,'剥离右边的空白','='*20)
sr=s.rstrip()
print(sr)


