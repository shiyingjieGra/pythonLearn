import itertools
import sys
import threading
import time

from openai import OpenAI

client = OpenAI(api_key="sk-3536851703fd4db6a714f2d9c6b7d638", base_url="https://api.deepseek.com")


def show_loading(stop_event, text="AI思考中"):
  for char in itertools.cycle("|/-\\"):
    if stop_event.is_set():
      break
    sys.stdout.write(f"\r{text} {char}")
    sys.stdout.flush()
    time.sleep(0.1)
  sys.stdout.write("\r" + " " * (len(text) + 2) + "\r")
  sys.stdout.flush()

message = [
  {
    "role": "system", "content": "You are a helpful assistant",
  }
]

print('欢迎来到我的AI，请输入你的请求：')


while True:
  user_input = input("> ")
  message.append({
    "role": "user",
    "content": user_input
  })

  stop_event = threading.Event()
  loading_thread = threading.Thread(target=show_loading, args=(stop_event,))
  loading_thread.start()

  try:
    response = client.chat.completions.create(
      model="deepseek-v4-pro",
      messages=message,
      max_tokens=1024,
      temperature=0.7,
      stream=False
    )
  finally:
    stop_event.set()
    loading_thread.join()

  print(response.choices[0].message.content)