from  HttpClient import HttpClient
import re
import threading

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




urlStr = raw_input("url:")
urlList = urlStr.split("/")
pathdir = urlList[len(urlList)-1]
v = HttpClient()
value = v.Get(urlStr,urlStr)
r1 = re.compile(r"http://\S*\.jpe*g")
srcList = re.findall(r1,value)
  #print value
print srcList

threads = []
i = 1
j =len(srcList)
for t in srcList:
    threads.append(getMyimg(i,j))

for tt in threads:
    tt.start()

#for path in srcList:
#	if not "__jpeg" in path:
#		v.DownloadFile(path,"/Users/zhouxq/images/"+pathdir)
#		print path


