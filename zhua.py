import re  
import urllib  
  
# Download picture and save in disk  
def downImg(url, dirPath, name):  
    fr = urllib.urlopen(url)  
    stream = fr.read(-1)  
    fr.close()  
    print dirPath+'/'+name  
    fw = open(dirPath+'/'+name, 'w')  
    fw.write(stream)  
    fw.close()  
  
def getPageCode(url, fromCharset, toCharset):  
    fr = urllib.urlopen(url)  
    pageCode = fr.read()  
    fr.close()  
    return pageCode  
  
def getImgUrl(pageCode):  
    pattern = re.compile(r'http\://[\w\-\./]+\.jpg')  
    return re.findall(pattern, pageCode)  
  
def main():  
    dirPath = '/home/damin/img'  
    nameEnding = 1  
    start = 'http://www.22mm.cc/mm/qingliang/'  
    allUrl = [start+'index.html']  
    x = 2  
    while x<=10:  
        allUrl += [start+'index_'+str(x)+'.html']  
        x += 1  
    for url in allUrl:  
        # 1. get page code   
        print url  
        pageCode = getPageCode(url, 'gb2312', 'utf8')  
        # 2. get all img url  
        imgUrl = getImgUrl(pageCode)  
        # 3. download the picture  
        for src in imgUrl:  
            filename = 'MM'+ str(nameEnding) +'.jpg'  
            nameEnding += 1  
            downImg(src, dirPath, filename)  
  
if __name__ == '__main__':  
    main()  