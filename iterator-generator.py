import sys

list = [1, 2, 3, 4, 5]

iterator = list.__iter__()
while True:
    try:
        print(iterator.__next__(), end=" ")
    except StopIteration:
        break

print()

def generator(maxNum):
    while maxNum > 0:
        try:
            yield maxNum
            maxNum -= 1
        except StopIteration:
            break
gen = generator(10)

while True:
    try:
        print(next(gen), end=" ")
    except StopIteration:
        sys.exit()