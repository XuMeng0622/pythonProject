# 导入 requests 包
import requests
from requests import request

# # 发送请求
# x = requests.get('https://www.runoob.com/')git
#
# # 返回 http 的状态码
# print(x.status_code)
#
# # 响应状态的描述
# print(x.reason)
#
# # 返回编码
# print(x.apparent_encoding)
# 导入 requests 包

# 发送请求
# x = requests.get('https://www.runoob.com/try/ajax/json_demo.json')
x = requests.request('GET', 'https://www.runoob.com/try/ajax/json_demo.json')
# x = requests.req


# 返回 json 数据
print(x.json())