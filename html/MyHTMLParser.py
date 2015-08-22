from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.nodes = []
        self.node ={}
        self.findtag = ""
        self.currentTag = ""
        self.noTagEnd = False;
        self.nodeAttr = {}
        HTMLParser.__init__(self)
    def handle_starttag(self,tag,attrs):
        #print "tag is {}  begin findtag:{} attrs {}".format(tag,self.findtag,attrs)
        self.currentTag =tag
        if self.findtag == tag:
            #print "begin find tg == current",tag,attrs
            self.findtag = tag
            self.node["tag"] = tag
            for attr in attrs:
                self.nodeAttr[attr[0]] =  attr[1]
            self.node["attrs"] = self.nodeAttr
            if self.noTagEnd:
                self.nodes.append(self.node)
            self.nodeAttr ={}
        else:
            pass
#print "findTag {}  tag {}",self.findtag,tag

    def handle_data(self,data):
    #print "data
        if self.findtag == self.currentTag:
            self.node["data"] = data
        #print "data  self node ",self.currentTag," data is ",data
        #else:
        #   print  "data  else ....self node ",self.currentTag," data is ",data

    def handle_endtag(self,tag):
       
        if self.findtag == tag:
            #self.nodes.append(tag)
            
            if not self.noTagEnd:
                self.nodes.append(self.node)
                self.node["endtag"] = tag
            #print "end  self node ",self.currentTag," tag is ",tag
            self.node={}
    
    
    def handle_data_me(self,data,tag,findtag):
        #print data
        if findtag == tag:
            print self.currentTag
            self.nodes.append(data)

    def get_nodes(self):
        return self.nodes

    def feed(self,data,findtag = None,noTagEnd = False):
        if noTagEnd:
            self.noTagEnd = noTagEnd
        if findtag is None:
            self.findtag = "html"
        else:
            self.findtag = findtag
        self.rawdata = self.rawdata + data
        self.goahead(0)


if __name__ == "__main__":

    htmlStr = "<html><body><h1 align='center' id ='think'>sdafdas</h1><tr><td id ='t1' color='red'>tdiiii</td><td>td2222</td></tr><input  name='aaa' value='333' /><input tytpe='text' ></body></html>"
    htmlStr2= '<body><h1>asdfads</h1><tr><td>td1<td><td>t2</td></tr><input type="image" src="http://chuantupian.com/8/uploads/2015/08/221778_10.jpg" onclick="window."n false;"></body>'
    parse = MyHTMLParser()
    #z = parse.get_starttag_text()
    #print z
    parse.feed(htmlStr2,"input",False)
    nodes = parse.get_nodes()
    print nodes
	#for node in nodes:
	#    if len(node["attrs"]) > 0:
    #        print "attrs",node["attrs"][0]
    #z = parse.get_tags()
    #print nodes[0]['attrs'][0]


