import requests
import re
from requests_html import HTMLSession
from requests_html import HTML
from bs4 import BeautifulSoup
#import mysql.connector
#from sklearn import tree
#from unidecode import unidecode

# Json To dctr
import json
class Payload(object):
	def __init__(self, j):
		self.__dict__ = json.loads(j)

# values Init
page = 0
max_result = 10
city = "tehran"
subCity1 = "تهران"
subCity2 = "ازگل"
category = "املاک-مسکن"
url = 'https://divar.ir/{}/{}/{}/browse/{}/?place=6,53&v05=0,1'.format(city,subCity1,subCity2,category)

# subject = "خوابگاه"

# objects Init
session = HTMLSession()

# Init Arrays
PostLists = []
Description = []


def parseTag(Tag,Type):
    # Subject find on Advertising Tag
    if Type == 'PostList':
        # Parse Tag
        a = Tag.text.replace('window.production = true; window.__PRELOADED_STATE__ = ','').strip()

        # return Json
        return eval(a[:-1])


while page <= max_result :
    # Next Page
    page += 1

    # requests divar.ir And return Page
    r = session.get(url+'&page='+str(page))

    try:
        # HTML parse
        Script = r.html.find('script')[-5]

        temp = Payload(parseTag(Script,'PostList')).browse['postList']

        # check len ListPost
        if len(temp) < 1 :
            break

        print('find {} item'.format(len(temp))

        # Get PostList
        PostLists.append(temp)

    except Exception as e:

        break
