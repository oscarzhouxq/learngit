from  HttpClient import HttpClient
import re

v = HttpClient()
value = v.Get("http://www.baidu.com","http://www.baidu.com")
r1 = re.compile(r"http://.+?jpeg")
srcList = re.findall(r1,value)
  #print value
print srcList
for path in srcList:
	if not "__jpeg" in path:
		v.DownloadFile(path,"f:/imagestest2")
		print path