#/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
print(data)
with open('/Users/sabrinaroy/python_learn/test/note.txt', 'w') as f:
	f.write(str(data))
