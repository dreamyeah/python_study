import requests

# r = requests.get('https://kyfw.12306.cn/otn/', verify=True)
# print r.text

print '----------------------'

r = requests.get('https://github.com',verify=True)
print r.text


print '----------------------'
r = requests.get('https://kyfw.12306.cn/otn/', verify=False)
print r.text

print '----------------------'
proxies = {
  "https": "http://127.0.0.1:4433"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print r.text