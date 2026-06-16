### 做一个简单的斐波那契函数


def fib(loopNum=None, maxNum=None):
  ### 这是一个斐波那契函数
  ### loopNum 表示循环次数，如果为0，则取最大值，否则，取循环次数的数组
  ### maxNum 最大值，如果当前值大于最大值，则停止
  ### 返回一个斐波那契数列

  if loopNum is None or maxNum is None:
    print("参数不足，请按以下方式调用：")
    print("  fib(loopNum, maxNum)")
    print("  - loopNum：循环次数；为 0 时按 maxNum 生成数列")
    print("  - maxNum：上限值，超过该值则停止")
    print("示例：fib(0, 100) 或 fib(10, 0)")
    return []

  if loopNum < 0 or maxNum < 0:
    return []

  isUseMaxNum = False
  if loopNum == 0:
    isUseMaxNum = True
  fibArray = []
  if isUseMaxNum:
    initNum = 0
    nextNum = 1
    fibArray.append(initNum)
    while nextNum < maxNum:
      fibArray.append(nextNum)
      initNum, nextNum = nextNum, initNum + nextNum

  else:
    initNum = 0
    nextNum = 1
    fibArray.append(initNum)
    for i in range(loopNum):
      fibArray.append(nextNum)
      initNum, nextNum = nextNum, initNum + nextNum

  return fibArray

print(fib(0, 100))

print(fib(10, 0))

print(fib())