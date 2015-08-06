import cookielib, urllib, urllib2
import os

class HttpClient:
  __cookie = cookielib.CookieJar()
  __req = urllib2.build_opener(urllib2.HTTPCookieProcessor(__cookie))
  __req.addheaders = [
    ('Accept', 'application/javascript, */*;q=0.8'),
    ('User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)')
  ]
  urllib2.install_opener(__req)

  def Get(self, url, refer=None):
    try:
      req = urllib2.Request(url)
      if not (refer is None):
        req.add_header('Referer', refer)
      return urllib2.urlopen(req).read()
    except urllib2.HTTPError as e:
      return e.read()

  def Post(self, url, data, refer=None):
    try:
      req = urllib2.Request(url, urllib.urlencode(data))
      if not (refer is None):
        req.add_header('Referer', refer)
      return urllib2.urlopen(req).read()
    except urllib2.HTTPError as e:
      return e.read()

  def Download(self, url, file):
    output = open(file, 'wb')
    output.write(urllib2.urlopen(url).read())
    output.close()

#  def urlencode(self, data):
#    return urllib.quote(data)

  def getCookie(self, key):
    for c in self.__cookie:
      if c.name == key:
        return c.value
    return ''

  def setCookie(self, key, val, domain):
    ck = cookielib.Cookie(version=0, name=key, value=val, port=None, port_specified=False, domain=domain, domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
    self.__cookie.set_cookie(ck)

  def  DownloadFile(self,sourceFile,localPath):
    if not os.path.exists(localPath):
      print localPath
      os.mkdir(localPath)
    try:
      
      filename = os.path.basename(sourceFile)
      localPathFileName = localPath+"/"+filename
      print filename
      return urllib.urlretrieve(sourceFile,localPathFileName)
    except Exception as e:
      return e

#self.__cookie.clear() clean cookie
# vim : tabstop=2 shiftwidth=2 softtabstop=2 expandtab


if __name__ == "__main__":
  v = HttpClient()
  #data = {"username":"ZMB222","password":"123456"}
  #value = v.Post("http://eserviceuat.prlife.com.cn:7001/eservice/account/login.action?action=login",data,"http://eserviceuat.prlife.com.cn:7001/eservice/account/login.action?action=init")
  #print(value)
  #z = v.DownloadFile("http://imgsrc.baidu.com/forum/w%3D580/sign=6b12a1088718367aad897fd51e738b68/1e29460fd9f9d72abb1a7c3cd52a2834349bbb7e.jpg","f:/imagestest")
  
  import re
  #baidu tieba
  #value = v.Get("http://tieba.baidu.com/p/2166231880","http://tieba.baidu.com/p/2166231880")
  #r1 = re.compile(r"http://imgsrc.baidu.com/forum/w%3D580/sign=[a-z0-9]+/[a-z0-9]+\.jpg")
  #cl
  value = v.Get("http://www.baidu.com","http://www.baidu.com")
  r1 = re.compile(r"http://.+?jpeg")
  #f  = open("f://file.txt","w+")
  #f.write(value)
  #f.close()
  srcList = re.findall(r1,value)
  #print value
  print srcList
  for path in srcList:
    v.DownloadFile(path,"f:/imagestest2")
    print path
