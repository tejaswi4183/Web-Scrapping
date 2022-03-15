import requests,bs4,webbrowser
import sys
import regex
x=sys.argv[1]
y='+'.join(x)
z='http://www.google.com/search?q='+y
r=requests.get(z)
b=bs4.BeautifulSoup(r.text)
c=b.select('a')
k=16
#p=int(input("Select one \n 1.LOGIN \n 2.BROWSE\n")))
for i in range(5):
	d=c[k].get('href')
	e='http://www.google.com/'+d
	webbrowser.open(e)
	k=k+1
