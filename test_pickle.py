import pickle
import pprint

# # 使用pickle模块将数据对象保存到文件
# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
#
# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)
#
# output = open('data2.pkl', 'ab')  #修改为追加写入
#
# # Pickle dictionary using protocol 0.
# pickle.dump(data1, output)
#
# # Pickle the list using the highest protocol available.
# pickle.dump(selfref_list, output, -1)
# output.close()

# #循环读取直至最后一行
with open('data2.pkl','rb') as f:
    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            f.close()
            break