import time

def write_file():
  with open('test_txt.txt', 'w', buffering=2, encoding='utf-8') as file:
    for i in range(5):
      file.write(f'写入：{i}')
      file.flush()
      time.sleep(1)
      file.write(f'({i})\n')

def read_file():
  with open('')

