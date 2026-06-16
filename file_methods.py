import time

with open('test_txt.txt', 'w', buffering=2, encoding='utf-8') as file:
  for i in range(5):
    file.write(f'写入：{i}')
    file.flush()
    time.sleep(1)
    file.write(f'({i})\n')