from HTMLParser import HTMLParser


import HTMLParser
class TitleParser(HTMLParser.HTMLParser):
    def __init__(self):
        self.currenttab =""
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self,tag,attrs):
        print "begin tag:",tag
        self.currenttab = tag
        
        if "input" == tag:
            print  "inputvvvv"
            for attr in attrs:
                print attr
    
    def handle_data(self,data):
        print "ddata ata:",data
    
    
    def handle_endtag(self,tag):
        
        print "end tag:",tag

def gettitle(self):
        return self.data

htmlStr = "<html><body><h1 align='center' id ='think'>sdafdas</h1><input  name='inputname' value='inputV' /></body></html>"

tp=TitleParser()
tp.feed(htmlStr)


