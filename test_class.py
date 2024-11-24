#!/usr/bin/python3

# class Parent:  # 定义父类
#     def __init__(self, age):
#         print('调用父类构造函数')
#         self.age = age
#
#     def myMethod(self):
#         print('调用父类方法')
#
#
# class Child(Parent):  # 定义子类
#     def myMethod(self):
#         print('调用子类方法')
#
# if __name__ == '__main__':
#     c = Child(2)  # 子类实例
#     # c.myMethod()  # 子类调用重写方法
#     super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法
#     print(dir(c))
#     help(c)

class Animal:
    def make_sound(self):
        print("Some generic animal sound")

    def __init__(self):
        print('aaaaa')

class Mammal(Animal):
    def __init__(self):
        super().__init__()  # 调用父类构造函数
        print('bbbbb')

    def make_sound(self):
        super().make_sound()
        print("Some mammal-specific sound")

class Dog(Mammal):
    def make_sound(self):
        super().make_sound()  # 这里假设是笔误，应为super().make_sound()
        print("Bark!")

    def __init__(self):
        super().__init__()  # 调用父类构造函数
        print('ccccc')

d = Dog()
d.make_sound()