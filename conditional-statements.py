if True:
  print('打印对的值')
else:
  print('打印错的值')

value = 1
match value:
  case 1 | 5 | 6:
    print('这是1或者5或者6')
  case 2:
    print('这是2')
  case _:
    print('都不是')