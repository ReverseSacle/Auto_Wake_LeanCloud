import requests
import sys
import time

if (len(sys.argv) >= 2):
    urls = sys.argv[1].split(',')
else:
    urls = "https://www.reversesacle.com/"  #Fill your site url(填写你的网站网址)

req = requests.get(urls)
print(f'网址唤醒状态:', 
      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
     )
