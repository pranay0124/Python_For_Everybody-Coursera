import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
address = input('Enter university: ')
url = serviceurl + urllib.parse.urlencode({'key':'42', 'address':  address})
data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)
info = info['results']
print ('Retrieving', url, '\nRetrieved', len(data), 'caracters')
for item in info:
    key = item['place_id']
print ('Place id:', key)