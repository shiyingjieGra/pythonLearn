tup1 = (1, 2, 3)
tup2 = 5, 6, 7

print(f'声明一个元组{tup1},{tup2}')

print(f'元祖类型{type(tup1)}')

array1 = [1, 2, 3, 'a', 'b', 'c']

print(f'列表转元组，列表为{array1}, 元祖为{tuple(array1)}')

print('元祖不可修改内容')
tup1[0] = 10  # 报错