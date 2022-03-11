import requests
import pandas as pd
import re
from bs4 import BeautifulSoup as soup
#Send get request:
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
html = requests.get('https://tripadvisor.com/Restaurants-g56003-Houston_Texas.html', headers=headers, allow_redirects = True, timeout=10)
print (html.status_code)

bsobj = soup(html.content,'lxml')

#print (bsobj)

hotel = []
for name in bsobj.findAll('a',{'class':'_15_ydu6b'}):
  hotel.append(name.text.strip())

Type = []
for t in bsobj.findAll('span',{'class':'_1p0FLy4t'}):
  if re.match('American', t.text):
    Type.append(t.text.strip()) 

ratings = []
for rating in bsobj.findAll('svg',{'class':'zWXXYhVR'}):
  ratings.append(rating['title'])

reviews = []
for review in bsobj.findAll('span',{'class':'w726Ki5B'}):
  reviews.append(review.text.strip())

price = []
for p in bsobj.findAll('span',{'class':'_1p0FLy4t'}):
  if re.match('\$', p.text):
    price.append(p.text.strip()) 

hotel = hotel[0:15]
Type = Type[0:15]
ratings = ratings[0:15]
reviews = reviews[0:15]
price = price[0:15]


d1 = {'Hotel':hotel,'Type':Type,'Ratings':ratings,'No_of_Reviews':reviews,'Price':price}
df = pd.DataFrame.from_dict(d1, orient='index')
df = df.transpose()
print(df)