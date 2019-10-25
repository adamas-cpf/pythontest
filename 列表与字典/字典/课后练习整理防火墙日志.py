import re
syslog='''UDP insideuser1  10.16.92.203:657 inside  10.16.51.86:657, idle 0:00:07, bytes 69572154, flags UIO
TCP insideuser1  10.16.90.13:22 inside  10.16.34.237:50377, idle 0:00:47, bytes 190455954, flags UIOB '''
syslog_split=re.split('\n',syslog)
syslog1=syslog_split[0]
syslog2=syslog_split[1]

A=re.match(".*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*bytes\s+(\d+).*flags\s+(\w*)\s*", syslog1)
# A=re.match('.*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*bytes\s+(\d{1,}).*flags\s+(\w*)\s*',syslog1)
# A=re.match('(\w\w\w)\s+(\w*)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*',syslog1)
print(A[1])
