import urllib2
import urllib
import cookielib
#m1
#response = urllib2.urlopen("http://www.baidu.com")
#print response.readline()

#m2
url = "http://eservice.prlife.com.cn/eservice/account/login.action?action=login"
cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
values = {"username":"zhouxiangqian","password":"123456"}
data = urllib.urlencode(values)
request = urllib2.Request(url,data)
#response = urllib2.urlopen(request);
response = urlOpener.open(request)
print response.read()
#session share
r = urlOpener.open("http://eservice.prlife.com.cn/eservice/user/customer.do?action=registration&ajax=true")

print r.read()