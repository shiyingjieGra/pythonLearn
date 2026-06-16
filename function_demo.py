from functools import reduce


def change(a):
	print(id(a))
	a = 10
	print(id(a)) # 非引用类型会生成新对象

change(5)

def changeList(list):
    if (len(list) >= 2):
		    list[1] = 102

numList = [1, 2]
changeList(numList)
print(numList) # 引用类型在函数内部改变会有变化

def changeTuple(tup):
    tup = ('a', 'b')
    return tup

tup = (1, 2)
print('修改前', tup, id(tup))
newTup = changeTuple(tup)

print('修改后', tup, id(tup))
print(newTup, id(newTup)) # 元祖为非引用类型


print('函数传参方式'.center(60, '='))

def normal(a, b):
  return (a, b)

print('正常传参只需要按照顺序传值即可', normal(1, 2))

def keywordFunc(a, b):
  print('关键字参数可以指定传参名称，不用遵循顺序', a, b)

keywordFunc(b = 1, a = 2)

def defaultFunc(a, b = 5):
  print('参数默认值会在未传参时赋值，有默认值参数需要放在无默认值参数后面', a, b)

defaultFunc(a = 3)

def uncertainFunc(a, *b):
  print('不定长参数会将剩余参数作为元祖放入*后的参数内', a, b)

uncertainFunc(1, 2, 3, 4)

def uncertainFunc2(a, **b):
  print('不定长参数**代表使用字典接收参数，但是这些不定长参数需要有参数名称', a, b)

uncertainFunc2(1, b = 2, c = 3, d = 4, e = 5)

def forceParamNameFunc(*, a, b):
  print('强制参数名函数需要参数传值时带入参数名，否则报错', a, b)

# forceParamNameFunc(1, 2) # 报错

forceParamNameFunc(a = 1, b = 2)

print('lambda函数使用'.center(60, '='))

computeAdd = lambda a, b: a + b

print('lambda为匿名函数', computeAdd(1, 2))

def funcFactory(n):
  return lambda a: a * n

doubleNumber = funcFactory(2)
tripleNumber = funcFactory(3)

print('可以使用lambda创建函数工厂', doubleNumber(2), tripleNumber(2))

numbers = [1, 2, 3, 4, 5]

print('lambda搭配数组使用，数组筛选大于2的内容', list(filter(lambda x: x > 2, numbers)))

print('lambda计算数字之和', reduce(lambda x, y: x + y, numbers))
