import datetime
import time

def show_time():
  """Hiển thị thời gian hiện tại."""
  now = datetime.datetime.now()
  formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Định dạng thời gian
  print(formatted_time)

while True:
  show_time()
  time.sleep(1) # Cập nhật mỗi giây