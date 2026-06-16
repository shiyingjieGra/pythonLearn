import operator

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'数组中间取值{testArray[2:6]}')

print(f'倒数取值{testArray[-4:]}')

del testArray[0]
print(f'删除第一个元素{testArray}')

print(f'数组长度{len(testArray)}')

print(f'数组拼接{testArray + [11, 12]}')

# for i in testArray:
#     print(i)

arr1 = [1 , 2 , 3]
arr2 = [4 , 5 , 6]
multiArr = [arr1, arr2]
print(f'多维数组{multiArr}')

for i in multiArr:
    for j in i:
        print(j, end=' ')
    print('')
    

print(f'{'列表比对'.center(60, '-')}')

arrCompare1 = [1, 2, 3]
arrCompare2 = [1, 2, 3]
arrCompare3 = [1, 2, 4]

print(f'列表比较{operator.eq(arrCompare1, arrCompare2)}')
print(f'列表比较{operator.eq(arrCompare1, arrCompare3)}')

print(f'1在数组出现次数{testArray.count(1)}')
print(f'2在数组出现次数{testArray.count(2)}')

arrExtend = ['a', 'b', 'c']
arrCompare1.extend(arrExtend)
print(f'列表扩展{arrCompare1}')

print(f'列表排序{sorted(arrExtend)}')

### 不在列表中会报错
# print(f'1在数组出现位置{testArray.index(1)}')

print(f'2在数组出现位置{testArray.index(2)}')

### 返回新列表，原列表不变
print(f'列表反转{testArray[::-1]}')

### 原列表改变
testArray.reverse()
print(f'列表方法反转{testArray}')

testArray.append(88)
print(f'列表插入一个值88{testArray}')

testArray.pop(0)
print(f'列表删除一个值{testArray}')

testArray.remove(88)
print(f'列表删除一个值88{testArray}')

testArray.clear()
print(f'列表清空{testArray}')

print('元组转数组', list((1, 2, 3)))