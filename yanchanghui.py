import requests
#import demjson
import json
from pprint import pprint
from urllib import request
import re
from bs4 import BeautifulSoup

url='http://www.228.com.cn/category/yanchanghui/'
rep=request.Request(url)
rep.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
resp=request.urlopen(rep)
buf=resp.read().decode('utf-8')
soup=BeautifulSoup(buf,'html.parser')
data=soup.find_all('span',class_=re.compile(r'category-boxb-ul-ft2'))
pages=int(data[0].get_text())

if pages /20!=0:
    pages=(pages/20)+1
else:
    pages=pages/20

s=requests.session()
i=1
while i<=pages:
    params = {'j': '1', 'p': i}
    haders = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
}
    req = s.get('http://www.228.com.cn/category/yanchanghui', params=params, headers=haders)
    ss = demjson.decode(req.text)
    for information in ss['products']:
        print information['shorta']
        print information['begindate']+'~'+information['enddate']
        print information['minprice']+'~'+information['maxprice']
        print information['cityname']
        print information['performer']
    i=i+1
