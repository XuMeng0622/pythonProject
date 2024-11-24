# --*-- coding: utf-8 --*--
import numpy as np
from functools import reduce
from itertools import count, product

counter =1

def doLotsOfStuff():
    global  counter
    for i in (1, 2, 3):
        counter += 1
        print('counter=%d', counter)

def test_function(a, b, *args):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print(__name__)

if __name__ == '__main__':
    # test_function(11,22,33,44,55,66,77,88,99)

    # dict1 = {'one':1, 'two':2, 'three':3}
    # dict2 = {'one':4, 'tmp':5}
    # dict1.update(dict2)
    # print(dict1)

    # a = '123'
    # b = '123'
    # print(a==b)
    # print(a is b)

    # doLotsOfStuff()
    # print(counter)

    # list = [1,2,3]
    # list.insert(2,[7,8,9])
    # print(list)

    # k = 1000
    # while k > 1:
    #     print(k)
    #     k = k / 2

    # dividend = 1
    # divide = int(input())
    # try:
    #     result = dividend / divide
    #     print(1, end='')
    # except ZeroDivisionError:
    #     print(2, end='')
    # except Exception:
    #     print(3, end='')
    # except:
    #     print(4, end='')

    # nums = set([1,2,2,3,3,3,4])
    # print(len(nums))

    # str1 = 'exam is a example'
    # str2 = 'exam'
    # print(str1.find(str2, 7))

    # sets = {1,2,3,4}
    # print(sets[2])  # 会报错，因为集合是无序的，不能支持通过索引来遍历元素

    # lists = [1,1,2,3,4]
    # lists.remove(1)
    # lists.extend([7,8,9])
    # print(lists)

    # a = 10
    # b = 1.0
    # c = (1,)
    #
    # print(type(a))
    # print(type(b))
    # print(type(c))
    # a = range(100)
    # print(a[::3])
    # for i in range(3):
    #     print(i)

    # str1 = 'hello,python'
    # str2 = 'python'
    # print(str1.index(str2))

    # name = '顺顺'
    # def f1():
    #     print(name)
    #
    # def f2():
    #     name = '峰峰'
    #
    # f1()
    # f2()
    # f1()

    # dicts = {}
    # dicts[(1,2)]=({3,(4,5)})
    # print(type(dicts[(1,2)]))

    # def w1():
    #     print('正在装饰')
    #     def inner():
    #         print('正在验证权限')
    #     return inner()
    #
    # w1()

    # tup = (1,2,[3,4])
    # # tup[2] += [5,6]
    # print(type(tup[2]))

    # def fun(a=(), b=[]):
    #     a += (1,)
    #     b.append(1)
    #     return a,b
    # print(fun())

    # dict = {}
    # dict[([1,2])] = 'abc' # 会报错
    # print(dict)

    # l = [1, 2, 'a', [1, 2]]
    #
    # # 将列表中的列表元素转换为元组
    # new_l = [tuple(x) if isinstance(x, list) else x for x in l]
    #
    # # 将处理后的列表转换为集合
    # result_set = set(new_l)
    #
    # print(result_set)

    # strs = 'abcd12efg'
    # print(strs.upper().title())

    # lis = ['1', '2', '3', '4']
    # print(lis[10:]) #返回[]

    # lis = [1,2,3]
    # a = id(lis)
    # lis += [4,5]
    # b = id(lis)
    # print(a==b)

    # for i in range(5):
    #     if i==2:
    #         pass
    #     print(i)

    # print([2] in [1,2,3])

    # str1 ='ll'
    # str2 = ''
    # if not str1:
    #     print(1)
    # elif not str2:
    #     print(2)
    # else:
    #     print(0)

    # class Base(object):
    #     count = 0
    #     def __init__(self):
    #         pass
    #
    # b1 = Base()
    # b2 = Base()
    #
    # b1.count = b1.count + 1
    # print(b1.count)
    # print(Base.count)
    # print(b2.count)

    # kvps = {'1':1, '2':2, '3':[3,4,5]}
    # theCopy = kvps.copy()
    # kvps['3'].append(6)
    # # sum = kvps['1'] + theCopy['1']
    # # print(sum)
    # print(kvps['3'])
    # print(theCopy['3'])

    # kvps = {'1':1, '2':2}
    # theCopy = kvps
    # kvps['1'] = 5
    # sum = kvps['1'] + theCopy['1']
    # print(sum)
    # print(kvps['3'])
    # print(theCopy['3'])

    # def adder(x):
    #     def wrapper(y):
    #         return x + y
    #     return wrapper
    #
    # adder5 = adder(5)
    # print(adder5(adder5(6)))

    # a = '123'
    # b = '123'
    # print(a==b)
    # print(a is b)
    # print(a+b)

    # print('\n'.join(['a', 'b', 'c']))

    # a, *b, c = range(10)
    # print(a, b, c)

    # tup = (1,(2,3))
    # a,b,c = tup #会报错， 因为元组的元素个数不匹配
    # print (a,b,c)

    # lis = ['1', '2']
    # a, b = list(map(int, lis))
    # print(a, b)

    # a = map(lambda x:x**3,[1,2,3])
    # print(list(a))

    # class Foo():
    #     def __init__(self):
    #         pass
    #
    #     def __getitem__(self, pos):
    #         return range(0,30,10)[pos]
    #
    # foo = Foo()
    # print(type(foo)) # <class '__main__.Foo'>
    # print(foo[0])
    # for i in foo:
    #     print(i)
    # print(len(foo)) # 会报错，因为Foo类没有实现__len__方法

    # truple = (1,2,3)
    # print(truple*2)

    # def dec(f):
    #     n = 3
    #     def wrapper(*args, **kwargs):
    #         print(*args, **kwargs)
    #         return f(*args, **kwargs)*n
    #     return wrapper
    #
    # @dec
    # def foo(n):
    #     return n*2
    #
    # print(foo(2))

    # def change_list(nums):
    #     nums.append('c')
    #     print(nums)
    # str1 = ['a', 'b']
    # change_list(str1)
    # print(str1)

    # res = []
    # for i in 'python':
    #     if i == 'h':
    #         continue
    #     res.append(i)
    # print(''.join(res))

    # a = '12'
    # b = '12'
    # # print(a is b)
    # # print(a == b)
    # # print(id(a) == id(b))    # True 因为a和b指向的是同一个字符串对象
    # print(dir(a))

    # print(reduce(lambda x,y:x+y, range(1,101)))
    # print(sum(range(1,101)))

    # random_numbers = np.random.randn(5)
    # print(random_numbers)

    # str1 = '你好，世界！'
    # print(str1)

    # a = 1
    # print(id(a))
    # a = 2
    # print(id(a))

    # s = "ajldjlajfdljfddd" #去重并从小到大排序输出
    # set_s = set(s)
    # list_s = sorted(set_s)
    # print(''.join(list_s))

    # lambda_func = lambda x, y : x*y
    # print(lambda_func(2,3))

    # dic = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
    # print(dic.items())
    # l = sorted(dic.items(), key=lambda x: x[0], reverse=False)
    # print(dict(l))

    #filter方法求出列表所有奇数并构造新列表
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # l = filter(lambda x: x % 2 == 1, a)
    # print(list(l))

    # l1 = [1,2,3]
    # l2 = [4,5,6]
    # print(l1+l2)
    # l1.extend(l2)
    # print(l1)

    # a = " hehheh " #去除收尾空格
    # print(a.strip())

    # a = [i for i in range(10)]
    # print(type(a))

    # print(type(range(10)))

    # dic = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
    # l = sorted(dic.items(), key=lambda x: x[0], reverse=False)
    # print(dict(l))

    # def send(path):
    #     print('send')
    #
    # def click(path):
    #     print('click')
    pass

    print('hello world')

