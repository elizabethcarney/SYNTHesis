# EXPERIMENTING WITH HTTP GETTING/PUSHING
# HackHer 2019
# Elizabeth Carney

#Key: tAsLon5bqbHdFNzca01BlkGeyCGGv9EX

core1 = "https://jukehost.co.uk/api/audio/f77338f46acb3e6ae40cc7c7391a8fc898a3ca39/4a9e1fda912"

import requests
import time

key = "tAsLon5bqbHdFNzca01BlkGeyCGGv9EX"
url = "https://raw.githubusercontent.com/shoenig17/shoenig17.github.io/master/boat.mp3"
service = "service"
reason = "reason"
message = "hello there"
vol = "50"

#get
#r = requests.get('http://192.168.1.72:8090/volume')
#answer = r.text

#post
#r = requests.get('http://192.168.1.72:8090/volume')
#print(r.text)
#p = requests.post('http://192.168.1.72:8090/speaker', data = {'volume':'35'})

payload = "<play_info><app_key>" + key + "</app_key><url>" + url + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + vol + "</volume></play_info>"
p = requests.post('http://192.168.1.72:8090/speaker', data=payload)
#print(p)

#r = requests.get('http://192.168.1.72:8090/volume')
#print(r.text)

#volCommand = "<volume>"+str(vol)+"</volume>"
#v = requests.post('http://192.168.1.72:8090/volume', volCommand)
#print(v)

#p = requests.get('http://192.168.1.72:8090/volume')
#print(p.text)

time.sleep(2)

p = requests.get('http://192.168.1.72:8090/standby')
#print(p.text)

#payload
#payload = {'key1': 'value1', 'key2': 'value2'}
#r = requests.get('https://httpbin.org/get', params=payload)
