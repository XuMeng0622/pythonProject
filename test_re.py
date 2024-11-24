#!/usr/bin/python3
import re

# line = "Cats are smarter than dogs"
# # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# # (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")

# phone = "2004-959-559 # 这是一个电话号码"
#
# # 删除注释
# num = re.sub(r'#.*$', "", phone)
# print("电话号码 : ", num)
#
# # 移除非数字的内容
# num = re.sub(r'\D', "", phone)
# print("电话号码 : ", num)

# !/usr/bin/python

# import re
#
#
# # 将匹配的数字乘以 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)
#
#
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))

# import re
# pattern = re.compile(r'\d+([a-z]+)\d+')                    # 用于匹配至少一个数字
# m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
# print( m )
# 
# m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
# print( m )
# 
# m = pattern.match('one12twothree34four', 3, 15) # 从'1'的位置开始匹配，正好匹配
# print( m )                                        # 返回一个 Match 对象
# print(m.group(0))   # 可省略 0
# print(m.start(0))   # 可省略 0
# print(m.end(0))   # 可省略 0
# print(m.span(0))    # 可省略 0

import re

# print(re.split('\W+', 'runoob, runoob, runoob.'))
# print(re.split('(\W+)', ' runoob, runoob, runoob.'))
# print(re.split('\W+', ' runoob, runoob, runoob.', 2))
# print(re.split('a*', 'hello world'))  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割

url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'

patt = re.compile(r'(\d{4}-\d{1,2}-\d{1,2})')
m =patt.findall(url)
print(m)