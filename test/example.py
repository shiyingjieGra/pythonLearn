def greet():
  print('执行了一个方法')

if __name__ == "__main__":
  print('脚本直接执行')
  greet()
else:
  print(f'外部调用执行{__name__}')