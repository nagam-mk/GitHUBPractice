import re,urllib
import urllib.request
u=urllib.request.urlopen('https://www.redbus.in/info/contactus')
text=u.read()
city=re.findall('[A-Z]+[a-z]+[ ][-][ ]',str(text))
ph=re.findall('[+][9][1][6-9]\d{9}',str(text))
i=0
for n in city:
    print(n,ph[i])
    i=i+1
