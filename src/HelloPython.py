from urllib import request, parse
import json
import time
#add two numbers and return the sum
response = 1
while response == 1:
    try:
        url = 'http://localhost:5000/add'
        data = {'a': 1, 'b': 2}
        data = parse.urlencode(data).encode('utf-8')
        req = request.Request(url, data=data)
        response = 0
    except:
        time.sleep(1)
        response = 1
        continue