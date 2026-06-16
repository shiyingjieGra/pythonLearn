import time

def print_progress_bar ():
  for i in range(101):
    loadingArray = ['/', '-', '\\', '|']
    loadingTag = loadingArray[i % 4]
    if i == 100:
      loadingTag = ''
    bar = '[' + '=' * (i // 2) + loadingTag + ' ' * (50 - i // 2) + ']'
    print(f'\r{bar} {i:3}%', end='', flush=True)
    # print(f'\r{loadingTag} building...', end='', flush=True)
    time.sleep(0.2)
  print(f'\n完成')



testString = 'Hello, World!'

print(testString[:5])

# print_progress_bar()
print('M' in testString)

print('M' not in testString)

print('---------------------------各种符号使用-----------------------------------')

print('这是一个数字%d， 这是一个字符串%s' %(1, 'test'))
print('%(name)s 字典映射' % {'value' : 'test', 'name' : 'test1111'})

### 第一个数字为整个数字占用宽度，第二个数字为小数精度，第三个数字为输出浮点数
print('%*.*f' % (8, 4, 3.1415926))

print('%-10s 左对齐' % 'hi')
print('%10s 右对齐' % 'hi')

print('%+d 正数前面加正号' % 5)

print('% d 正数前面加空格 \n% d 负数前面不加空格' % (2, -2))

print('%#o 显示进制 \n %o 不显示进制前缀' % (8, 8))

print('%05d 零填充宽度' % 5)

print('%6.2f 最小宽度及精度，宽度为6，精度为2' % 3.1415926)

print('--------------------------三引号使用-------------------------------')

htmlString = '''
<html>
  <head>
    <title>test</title>
  </head>
  <body>
    <h1>hello, world</h1>
    <span>[\t]这是制表符</span>
  </body>
</html>
'''

print(htmlString)

print('字符串工具'.center(60, '-'))

print('capitalize 首字母大写\n %s' % 'hello, world'.capitalize())

print('center 指定宽度居中\n %s' % 'center string'.center(20, '*'))

print('count 统计字符串出现次数\n hello world前面五个字段中o出现次数为 %d' % 'hello world'.count('o', 0, 5))

codingString = '我的字符串是这个'
decodingString = codingString.encode('utf-8')

print('encode 编码\n %s 编码后为 %s' % (codingString, codingString.encode('utf-8')))

print('decoding解码 \n %s' % decodingString.decode('utf-8'))

print('endswith 判断字符串是否以指定字符串结尾\n test.dat是否以.dat结尾 %s' % 'test.dat'.endswith('.dat'))

print('expandtabs 将制表符转换为空格\n %s' % '[\t]'.expandtabs())

print('find 查找字符串\n o在hello world中位置为 %s' % 'hello world'.find('o'))

print('isalnum 判断字符串是否都是数字或者字母组成\n %s' % 'helloworld1'.isalnum())

print('isalpha 判断字符串是否都是字母或者中文组成\n %s %s' % ('这是中文，但是有符号', '这是中文，但是有符号'.isalpha()))

print('isdigit 判断字符串都是数字组成\n %s' % '11123213232323'.isdigit())

print('islower 判断字符串是否都是小写字母组成\n %s' % 'hello World1'.islower())

print('isnumeric 判断字符串是否都是数字组成\n %s' % '一百二十二'.isnumeric())


