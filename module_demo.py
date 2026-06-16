import sys

from test.example import greet

import test.example

from function_demo import change 

for i in sys.argv:
  print(f'参数为：{i}')


# change(10)

print('直接引入方法是不会触发运行时校验')
greet()

print('引入模块在导入时会触发运行时校验')

test.example.greet()