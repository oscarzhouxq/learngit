from  HttpClient import HttpClient
import re

urlStr = raw_input("url:")
urlList = urlStr.split("/")
pathdir = urlList[len(urlList)-1]
v = HttpClient()
value = v.Get(urlStr,urlStr)
r1 = re.compile(r"http://\S*\.jpe*g")
srcList = re.findall(r1,value)
  #print value
print srcList
for path in srcList:
	if not "__jpeg" in path:
		v.DownloadFile(path,"/Users/zhouxq/images/"+pathdir)
		print path


