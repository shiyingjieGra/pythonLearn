from operator import itemgetter
from typing import OrderedDict, Self


class Queue :
  def __init__(self):
    self.queue = []

  def enqueue(self, item):
    if isinstance(item, list) or isinstance(item, tuple):
      self.__enqueue_list__(item)
    else:
      self.queue.append(item)
      
  def dequeue(self):
    if len(self.queue):
      return self.queue.pop(0)

  def print_queue(self):
    print(f'{self.queue}')

  def __enqueue_list__(self, item):
    for l in item:
      self.queue.append(l)

queue1 = Queue()

queue1.enqueue(1)

queue1.print_queue()

queue1.enqueue([2, 3, 4])

queue1.print_queue()

queue1.enqueue((5, 6, 7))

queue1.print_queue()

print(f'拿出一个：{queue1.dequeue()}')

queue1.print_queue()


