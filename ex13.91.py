import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

countlist = list()
address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
commentlen = info['comments']
print('Count', len(commentlen))
for item in commentlen:
    countlist.append(item['count'])
print(sum(countlist))
