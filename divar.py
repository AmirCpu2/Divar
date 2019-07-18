import requests
import re
from requests_html import HTMLSession
from requests_html import HTML
# from bs4 import BeautifulSoup
#import mysql.connector
#from sklearn import tree
#from unidecode import unidecode

# values Init
page = 0
max_result = 1
city = "tehran"
subCity1 = "تهران"
subCity2 = "ازگل"
category = "املاک-مسکن"
url = 'https://divar.ir/{}/{}/{}/browse/{}/?place=6,53'.format(city,subCity1,subCity2,category)

# subject = "خوابگاه"

# objects Init
session = HTMLSession()

# Init Arrays
Advertising = []
Subject = []
Description = []
Photo = []
Paymant = []
Day = []
Phone = []
Time = []
LinkPage = []

def parseTag(Tag,Type):
    # Advertising find on Page Tag $ content
    if Type == 'Advertising':
        return Tag.html.find('.post-card')

    # Subject find on Advertising Tag
    if Type == 'Subject':
        return Tag.find('h2', first=True).text

    # Description find on Advertising Tag
    if Type == 'Description':
        return Tag.find('.column.content', first=True)

    # Photo find on Advertising Tag
    if Type == 'Photo':
        try:
            return Tag.find('.image.column', first=True).find('.ui.image', first=True).attrs['src']
        except:
            return 'not found'

    #Paymant find on Advertising Tag
    if Type == 'Paymant':
        return ''

    if Type == 'Json':
        return Tag.find('script',first=True)


while page <= max_result :
    # Next Page
    page += 1

    # requests divar.ir And return Page
    r = session.get(url+'& page='+str(page))

    # parse Tags
    tmp = parseTag(r,'Advertising')

    # check len Advertising
    if len(tmp) < 1 :
        break

    print(str(len(tmp))+'mord peyda shod')

    # insert tag to list
    Advertising.append(tmp)

for ListPage in Advertising:
    for item in ListPage:
        print(parseTag(item,'Subject'))
        print(parseTag(item,'Description'))
        print(parseTag(item,'Photo'))
        print(parseTag(item,'Paymant'))
        print(parseTag(item,'Json'))
