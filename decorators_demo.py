import time
print('装饰器'.center(60, '-'))

def timer_decorators(func):
    def wrapper (*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'当前函数执行时间为 {end_time - start_time:.2f}')
    return wrapper

@timer_decorators
def doSomething ():
    time.sleep(1)

doSomething()

print('装饰器循环执行函数'.center(60, '-'))

def cycle_run_func(time_num):
  def decorator(func):
    def wrapper(*args, **kwargs):
      for _ in range(time_num):
        func(*args, **kwargs)
    return wrapper
  return decorator

@cycle_run_func(5)
def printSomeThing():
  print('重复打印')

printSomeThing()


print('类装饰器'.center(60, '-'))

def class_decorator(cls):
  class Wrapper:
    def __init__(self, *args, **kwargs):
      self.wrapped = cls(*args, **kwargs)

    def __getattr__(self, name):
      print(f'获取属性{name}')
      return getattr(self.wrapped, name)

    def __str__(self):
      return str(self.wrapped)

    def display(self):
      print('调用display方法')
      self.wrapped.display()
      print('调用结束')
  return Wrapper
  

@class_decorator
class TestClass:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  
  def __repr__(self):
    return f'[√]{self.a}and{self.b}'
    
  def display(self):
    print('展示什么东西')

my_class = TestClass(a = 1, b = 2)

my_class.display()

print(f'打印属性{my_class.a}')

print(my_class)


print('多重装饰器'.center(60, '='))

def Decorator1(func):
  def wrapped(*args, **kwargs):
    print('Decorator1')
    func(*args, **kwargs)
  return wrapped

def Decorator2(func):
  def wrapped(*args, **kwargs):
    print('Decorator2')
    func(*args, **kwargs)
  return wrapped

@Decorator1
@Decorator2
def doSomeThing():
  print('打印什么东西')

doSomeThing()