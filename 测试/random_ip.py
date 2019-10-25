#导入随机数模块
import random
import string
#随机产生IP地址四个字段的数字
part1 = random.randint(1,255)
part2 = random.randint(1,255)
part3 = random.randint(1,255)
part4 = random.randint(1,255)
#把数字拼接成字符串
random_ip = str(part1) +  '.' + str(part2) +  '.'+ str(part3) +  '.' + str(part4)
#打印出随机IP
print(random_ip)