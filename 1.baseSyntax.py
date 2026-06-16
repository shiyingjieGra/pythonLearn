#!/usr/bin/python3
import keyword
import sys
from sys import argv,path
def is_valid_identifier(name):
  try:
    # f将字符串中的变量替换为变量的值，exec函数执行字符串中的代码，如果字符串中的变量不存在，则抛出异常
    exec(f"{name} = None")  # 尝试将变量赋值为None，测试是否是有效的标识符
    return True;
  except: 
    return False;

'''
print(is_valid_identifier('abc'))
print(is_valid_identifier('123'))
print(is_valid_identifier('abc123'))
print(is_valid_identifier('abc-123'))
print(is_valid_identifier('abc 123'))
'''
print(keyword.kwlist)

exec('kk = None')

if (is_valid_identifier('abc')):
  print('abc is a valid identifier')
else:
  print('abc is not a valid identifier')

item_one = 1
item_two = 2
item_three = 3
total = item_one +\
        item_two +\
        item_three
print(total)

print('这是一个换行符\n换行了')
print(r'这是一个换行符\n没有换行')

# input("\n\n按下enter键退出。")

x = 'runnoob';
sys.stdout.write(x + '\n')

print('不换行print测试')
print('第一行', end='')
print('第二行', end='')

print('===================Python import mode=========================')
for name in sys.argv:
  print(name)
print('\n python路径为', sys.path)

print('===================Python import from=========================')
print(argv)
print('path', path)