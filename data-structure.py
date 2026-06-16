print('数组方法'.center(60, '='))

list1 = [1, 2, 3]
print(f'列表为：{list1}')

append_list = [4, 5]
list1.append(append_list)

print(f'向后添加一个数组{append_list}后，数组为{list1}')

list1.extend([6, 7])

print(f'扩充列表[6, 7]扩充后数组为{list1}')

list1.insert(1, 8)

print(f'第二位插入元素8，当前数组为{list1}')

list1.remove(1)

print(f'移除元素为1的第一个匹配元素，当前数组为{list1}')

list1.pop()

print(f'移除一个元素，如果没传则默认移除最后一个元素，当前数组为{list1}')

print(f'当前数组值为[4, 5]的位置为{list1.index([4, 5])}')

print(f'5在数组内数量为{list1.count(5)}')


list2 = [4, 2, 6, 2, 7, 7, 8]
list2.sort()

print(f'数组排序，排序后数组为{list2}')

list2.reverse()
print(f'数组翻转，当前数组为{list2}')

print(f'2在当前数组位置为{list2.index(2)}')

print(f'2在当前数组数量为{list2.count(2)}')

list_copy = list2[:]

print(f'复制出来的数组为{list_copy}')

list1.clear()

print('数组操作'.center(60, '='))

vec = [2, 4, 6]

print(f'原始数组为{vec}')

print(f'数组全部×2{[x*2 for x in vec]}')

print(f'转2维数组：{[[x * 2, x * 3] for x in vec]}')

print(f'小于5的元素筛选{[x for x in vec if x < 5]}')

vec2 = [6, 9, -10]
print(f'第二个数组{vec}')

print(f'双数组同时循环计算{[x * y for x in vec for y in vec2]}')

metrics = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12]
]

print(f'有一个4*3矩阵{metrics}')

print(f'变成3*4矩阵{[[metrics[y][x] for y in range(len(metrics))] for x in range(len(metrics[0]))]}')