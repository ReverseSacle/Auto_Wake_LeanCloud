import requests
import sys
import time


urls = sys.argv[1]
req = requests.get(urls)
print(f'网址唤醒状态:',
      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
     )
