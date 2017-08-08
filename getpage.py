#coding=utf-8
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://www.qq.com")

#print html
output = open('page.html', 'w')
output.write(html);
output.close()
