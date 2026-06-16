print('数组推导式'.center(60, '='))

array = [1, 2, 3, 4, 5]

print(f'数组内值全部变为双倍{[x * 2 for x in array]}')

dict = {x: x * 2  for x in array}
print(f'数组推导字典{dict}')

newSet = {x ** 2 for x in array}
print(f'数组推导集合{newSet}')

newTuple = tuple(x * 3 for x in array)
print(f'数组推导元祖{newTuple}')

print('字典推导式'.center(60, '='))

dict = {'a': 1, 'b': 2, 'c': 3}

newDict = {dict[key]: key for key in dict}

print(f'字典推导key value反转{newDict}')

newDict2 = {value: key for key, value in dict.items() if value > 1}

print(f'字典推导筛选值大于1{newDict2}')

dictArray = [key for key in dict]

print(f'字典推导数组{dictArray}')

dictSet = {key for key in dict}

print(f'字典推导集合{dictSet}')

dictTuple = tuple(key for key in dict)

print(f'字典推导元祖{dictTuple}')

