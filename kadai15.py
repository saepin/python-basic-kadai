# -*- coding: utf-8 -*-
"""kadai15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/saepin/10a9f9b3dc3dc8702758e355ce2e798b/kadai15.ipynb
"""

class Human:
   def __init__(self, name, age):

     self.name = name
     self.age = age
   def set_name(self, name):
     self.name = name

   def show_name(self):
     print(self.name)



human = Human("一郎", 3)

# 属性にアクセスし、値を出力する
print(human.name)
print(human.age)