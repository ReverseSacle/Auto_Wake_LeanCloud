import requests
import sys
import time

if (len(sys.argv) >= 2):
    urls = sys.argv[1].split(',')
else:
    #Fill your site which is for organization of comment(填写你的评论管理地址 (后台地址))
    #https://xxxxx.avosapps.us/
    urls = "https://www.reversesacle.com/"

req = requests.get(urls)
print(f'网址唤醒状态:', 
      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
     )
