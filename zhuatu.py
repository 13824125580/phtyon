import urllib2  
import urllib  
import re  
  
def getHtml(url):  
    page = urllib.urlopen(url)  
    html =  page.read()  
    return html  
  
def getJpg(html):  
    reg = r'"largeTnImageUrl":"(.+?\.jpg)",'  
    imgre = re.compile(reg)  
    imglist = re.findall(imgre, html)  
    x = 0  
    for imgurl in imglist:  
        print imgurl  
        #urllib.urlretrieve(imgurl, 'D:/test/%s.html' % x)  
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',  
        'Accept':'text/html;q=0.9,*/*;q=0.8',  
        'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',  
        'Accept-Encoding':'gzip',  
        'Connection':'close',  
        'Referer':'http://image.baidu.com/i?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1425134407244_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%AF%94%E5%9F%BA%E5%B0%BC%E7%BE%8E%E5%A5%B3&f=3&oq=b&rsp=-1'  
        }  
        timeout = 30  
        request = urllib2.Request(imgurl,None,header)  
        response = urllib2.urlopen(request,None,timeout)  
        str = response.read()  
        foo = open("./test/%s.gif" % x,"wb")  
        foo.write(str)  
        foo.close()  
        x += 1  
          
html = getHtml('http://image.baidu.com/i?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1425134407244_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%AF%94%E5%9F%BA%E5%B0%BC%E7%BE%8E%E5%A5%B3&f=3&oq=b&rsp=-1')  
print getJpg(html)
