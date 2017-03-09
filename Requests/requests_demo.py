#coding=utf-8
import requests
import json
r = requests.get('http://www.kaola.com')
print type(r)
print r.status_code
print r.encoding
print r.cookies


print '-------------------------------'
r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/head")
r = requests.options("http://httpbin.org/options")

print '-------------------------------'

payload = {'key1':'value1','key2':'value2'}
r = requests.get("http://httpbin.org/get",params = payload)
print r.url

print '-------------------------------'

payload = {'key1':'value1','key2':'value2'}
headers = {'content-type':'application/json'}
r = requests.get("http://httpbin.org/get",params = payload,headers = headers)
print r.url

print '-------------------------------'

payload = {'key1':'value1','key2':'value2'}
r = requests.post("http://httpbin.org/post",data = payload)
print r.text

print '-------------------------------'
payload = {'some':'data'}
r = requests.post("http://httpbin.org/post",data = json.dumps(payload))
print r.text

print '-------------------------------'

files = {'file':open('../Example/file1.txt','rb')}
r = requests.post("http://httpbin.org/post",files = files)
print r.text

# print '-------------------------------'
# with open('../Example/file1.txt') as f:
# 	requests.post("http://httpbin.org/post",data = f)
print '-------------------------------'
url = 'http://example.com'
r = requests.get(url)
print r.cookies
print r.cookies['example_cookie_name']


print '-------------------------------'
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url,cookies=cookies)
print r.text

print '-------------------------------'

requests.get('http://github.com',timeout = 0.01)