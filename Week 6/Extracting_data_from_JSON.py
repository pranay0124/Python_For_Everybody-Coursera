import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter url: ')
data = urllib.request.urlopen(url).read()
info = json.loads(data)
info = info['comments']
print ('Retrieving', url)
print('\nRetrieved')
print('Caracters:', len(data))
print('Count:', len(info))
num = 0
for item in info:
    num += int(item['count'])
print ('Sum:', num)