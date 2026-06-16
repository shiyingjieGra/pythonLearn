import inspect
class Memoize:
  def __init__(self, func):
    self.func = func
    self.cache = {}
    self.signature = inspect.signature(func)

  def _make_key(self, args, kwargs):
    bound_args = self.signature.bind(*args, **kwargs)
    bound_args.apply_defaults()
    # print(self.signature, bound_args)
    key_list = []
    for param_name in self.signature.parameters:
      if param_name in bound_args.arguments:
        value = bound_args.arguments[param_name]
        key_list.append(self._make_hashable(value))
    # key_args = tuple(self._make_hashable(arg) for arg in args)
    # key_kwargs = tuple(sorted((k, self._make_hashable(v)) for k, v in kwargs.items()))
    return tuple(key_list)
  
  def _make_hashable(self, obj):
    if isinstance(obj, list):
      return tuple(self._make_hashable(v) for v in obj)
    elif isinstance(obj, dict):
      return tuple(sorted((k, self._make_hashable(v)) for k, v in obj.items()))
    elif isinstance(obj, set):
      return tuple(sorted(self._make_hashable(v) for v in obj))
    else:
      return obj

  def __call__(self, *args, **kwargs):
    result_key = self._make_key(args, kwargs)
    if result_key in self.cache:
      return self.cache[result_key]
    result = self.func(*args, **kwargs)
    self.cache[result_key] = result
    return result

@Memoize
def addNum(a, b):
  print('函数相加')
  return a + b

print(addNum(a = 1, b = 2))
print(addNum(b = 2, a = 1))

@Memoize
def addList(list1, list2):
  print('数组相加')
  return list1 + list2

print(addList(list1 = [1, 2], list2 = [3, 4]))
print(addList([1, 2], [3, 4]))
print(addList(list2 = [3, 4], list1 = [1, 2]))


class MyClass:
  name = 'wwww'
  def __init__(self, a, b):
    self._a = a
    self.b = b
  
  @staticmethod
  def static_method():
    print('静态方法')

  @classmethod
  def class_method(cls):
    print(cls.name)

  @property
  def name(self):
    return self._a

  @name.setter
  def name(self, value):
    print('设置name', value)
    self._a = value

  # @name.setter
  # def name(self, value):
  #   print('设置值')
  #   self._name = value

my_class = MyClass(a = 1, b = 2)

MyClass.static_method()
MyClass.class_method()

print(my_class.name)

my_class.name = 5