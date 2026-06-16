orgFileContent = ''

with open('./list.py', 'r', encoding='utf-8') as file:
    orgFileContent = file.read()
    print(orgFileContent)

with open('./listCopy.py', 'w', encoding='utf-8') as file:
    orgFileContent += '\n这是一个拷贝文件'
    file.write(orgFileContent)

class Persion:
    def __init__(self):
        print('初始化一个对象')
        self.name = '张三'
        self.age = 18
    def __enter__(self):
        print('进入with初始化，我将生成一个对象')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'退出with，现在对象为{self.name}，{self.age}我将进行销毁')
        del self
        try:
            print(f'现在对象已经被销毁，对象为{self is None}')
        except Exception as e:
            print(f'发生异常{e}')

with Persion() as persion:
    print(f'现在对象为{persion.name}，{persion.age}')


### 这是一个计时器

class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        print(f'计时开始，当前时间为: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.start))}')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        start_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.start))
        end_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.end))
        print(f'计时结束：{end_str}，执行总耗时：{self.end - self.start:.2f} 秒')

with Timer() as timer:
    import time
    time.sleep(3)
    print('执行完毕')

### 使用contextmanager装饰器

from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    print(f'计时开始，当前时间为{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start))}')
    yield
    end = time.time()
    print(f'计时结束，当前时间为{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end))}，共计耗时{end - start:.2f}s')

with timer() as timer:
  import time
  print('沉睡4秒')
  time.sleep(4)