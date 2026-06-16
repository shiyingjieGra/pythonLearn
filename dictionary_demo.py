my_dict = { 1: 'a', 'a': 2, (3, 4): 'b'}

print(f'新建一个字典{my_dict}')

print(f'字典长度{len(my_dict)}')

print(f'字典中键为1的值{my_dict[1]},键为a的值{my_dict["a"]},键为(3,4)的值{my_dict[(3, 4)]}')

print(f'字典类型{type(my_dict)}')

print(f'创建新字典{dict.fromkeys((1, (3, 4)), 2)}')

del my_dict[(3, 4)]
print(f'删除键为(3,4)的键值对{my_dict}')

my_dict.clear()
print(f'清空字典{my_dict}')

new_dict = {1: 'a', 2: 'b', 3: 'c'}
for key in new_dict:
  print(f'字典的键为{key}, 字典的值为{new_dict[key]}')

print(f'返回视图对象{new_dict.items()}')

new_dict.setdefault(4, 'x')

print(f'设置键为4的默认值为x{new_dict}')

update_dict = {4: 'd', 5: 'e'}
new_dict.update(update_dict)
print(f'{update_dict}更新进字典{new_dict}')

print(f'字典取key{new_dict.keys()}')
print(f'字典取值{new_dict.values()}')

print(f'去除并删除一个键值对{new_dict.pop(1)}，取值后字典为{new_dict}')
# print(f'取字典内没有键的值会报错{my_dict[5]}')