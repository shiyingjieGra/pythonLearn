new_set = set()

print(f'创建一个空集合{new_set}')

new_set.update('python')

print(f'添加元素{new_set}，使用update会被拆包')

new_set.add('java')

print(f'添加元素{new_set}，使用add不会拆包')

new_set.update(['c++'], ('c#',))

print(f'如果是不可拆解的迭代对象，也不会被拆包{new_set}')

new_set.remove('c#')

print(f'删除元素c#{new_set}, remove不会拆包，如果元素不存在会报错')

new_set.discard('python')

print(f'删除元素python{new_set}, discard不会拆包，如果元素不存在不会报错')

print(f'pop会随机删除一个元素{new_set.pop()}')

print(f'集合长度{len(new_set)}')
print(f'集合类型{type(new_set)}')

print('集合操作'.center(60, '-'))

set1 = {'python', 'java', 'c#'}
set2 = {'c#', 'c++', 'c'}

print(f'现在有两个集合{set1}和{set2}')

print(f'两个集合差集{set1.difference(set2)}')

print(f'两个集合的交集{set1.intersection(set2)}')

print(f'判断set2是否为set1子集{set1.issubset(set2)}')

print(f'判断set1是否为set2超集{set1.issuperset(set2)}')

print(f'返回两个集合不重复的元素集合{set1.symmetric_difference(set2)}')

print(f'取两个集合并集{set1.union(set2)}')

print(f'&取两个集合交集{set1 & set2}')

print(f'|取两个集合并集{set1 | set2}')

print(f'-取两个集合差集{set1 - set2}')

print(f'^取两个集合不重复的元素集合{set1 ^ set2}')