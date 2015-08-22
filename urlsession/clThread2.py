#coding=utf-8
from  HttpClient import HttpClient
import re
import threading


#
class getMyimg(threading.Thread):
    def __init__(self,begin,end):
        threading.Thread.__init__(self)
        self.begin = begin
        self.end = end
    def run(self):
        for i in range(self.begin,self.end):
            if len(srcList) > 0:
                path = srcList.pop()
                if not "__jpeg" in path:
                
                    v = HttpClient()
                    v.DownloadFile(path,"/Users/zhouxq/images/"+pathdir)
                    print path

if __name__ == "__main__":
    urlStr = raw_input("url:")
    urlList = urlStr.split("/")
    pathdir = urlList[len(urlList)-1]
    v = HttpClient()
    value = v.Get(urlStr,urlStr)
    #r1 = re.compile(r"http://\S*\.jpe*g")
    from MyHTMLParser import MyHTMLParser
    parser = MyHTMLParser()
    value = value.decode('gbk').encode('utf-8')
    print value
    
   
    parser.feed(value,"input")
    nodes = parser.get_nodes()
    print nodes
    srcList = []
    for node in nodes:
        for attr in node["attrs"]:
            if attr == "src":
                srcList.append(node["attrs"][attr])
                #print node["attrs"][attr]


    threads = []
    i = 1
    j =len(srcList)
    for t in srcList:
        threads.append(getMyimg(i,j))

    for tt in threads:
        tt.start()
