import urllib.request,urllib.response,urllib.parse



#get方式
# response=urllib.request.urlopen('https://www.baidu.com')
# print(response.read().decode('utf-8'))

#post方式。#httpbin.org测试网址
# data=bytes(urllib.parse.urlencode({'1':'xxx','2':'cccc'}),encoding='utf-8')
# response = urllib.request.urlopen('https://httpbin.org/post',data=data)
# print(response.read().decode('utf-8'))


#超时
# try:
#     response = urllib.request.urlopen('https://httpbin.org/get',timeout=1)
#     print(response.status)
# except urllib.error.URLError as e:
#     print('urlerror,timeut')


# #网页和服务器中的资源及介绍
# response = urllib.request.urlopen('https://baidu.com')
# print(response.getheader('Server'))



url = 'http://www.douban.com'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 '
                 'Safari/537.36'}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))