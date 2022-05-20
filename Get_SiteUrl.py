import requests
import sys
import time


urls = sys.argv
print(urls)
req = requests.get(urls[0])
print(urls[0])
print(f'网址唤醒状态:',
      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
     )
