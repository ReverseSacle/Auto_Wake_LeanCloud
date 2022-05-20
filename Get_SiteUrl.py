import requests
import sys
import time

if (len(sys.argv) >= 2):
    urls = sys.argv[1].split(',')
else:
    #Fill your organization of comment for site url(填写你的评论管理地址 (后台地址))
    #https://xxxxx.avosapps.us/
    urls = "https://reversesacle.avosapps.us/"

req = requests.get(urls)
print(f'网址唤醒状态:', 
      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
     )
