import pickle, pprint

def open_file_func():
  str = input('请输入打开文本地址：')

  print(f'你输入的文本地址是：{str}')

  try:
    with open(str, 'r', encoding='utf-8') as file:
      print('文件内容为：')
      print(file.read())
  finally:
    print('打印完成')

def write_file_func():
  print('写入test_demo的内容')

  fileContent = input('> ')

  with open('test_demo.py', 'w', encoding='utf-8') as file:
    file.write('我输入了内容\n' + fileContent)

  print('写入完成')

def file_tell_seek_func():
  print("读取一个文件")
  with open('test_demo.py', 'w+', encoding='utf-8') as file:
    file.write('测试脚本\n第二行\n第三行')
    print('当前位置', file.tell())
    print(file.read())
    print("往前进一位")
    file.seek(0)
    print(file.read(1))
    print("打印一行")
    file.seek(0)
    print(file.readline())
    print("打印两行")
    file.seek(0)
    print(file.readlines(8))
    print("按照行读取：")
    file.seek(0)
    for line in file:
      print(line, end="")


def pickle_save():
  data = {
    'arr': [1, 2, 3, 4],
    'tup': ('a', 'b', 'c'),
  }

  with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

pickle_save()

def pickle_use():
  with open('data.pkl', 'rb') as file:
    data = pickle.load(file)
    pprint.pprint(data)

pickle_use()