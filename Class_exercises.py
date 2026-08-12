"""
写一个 Dog 类：
__init__ 接收 name 和 age，存到对象里
写一个 bark() 方法，打印 "[name]说：汪汪！我今年[age]岁了"
创建两个对象：dog1 = Dog("旺财", 3)、dog2 = Dog("来福", 2)
分别调用 bark()
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}说:汪汪！我今年{self.age}岁了")

dog1 = Dog("旺财", 3)
dog1.bark()
dog2 = Dog("来福", 2)
dog2.bark()