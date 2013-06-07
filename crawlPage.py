import re
import urllib
import sel
from lxml import etree
showPage=re.compile(r"http://www.youku.com/show_page/(.*)")
keywordPage=re.compile(r"http://v.youku.com/v_show/(.*)")
indexPage=re.compile(r"http://index.youku.com/(.*)")
def getIndexPage (url):
    m=showPage.match(url)
    if m:
        return (0,r"http://index.youku.com/vr_show/show"+m.group(1))
    m=keywordPage.search(url)
    if m:
        return (1,r"http://index.youku.com/vr_keyword/id_"+m.group(0))
    m=indexPage.search(url)
    if m:
        return (2,url)
    raise Exception("Non-youku page")

def crawlKeywordPage(link):
    return sel.getJSON(link)

def crawlShowPage(pagelink,indexlink):
    print pagelink
    showIndex=sel.getJSON(indexlink)
    page=urllib.urlopen(pagelink)
    data=page.read().decode('utf-8')
    dom=etree.HTML(data)
    page.close()
    episodes=dom.xpath(r"/html/body/div/div/div[2]/div/div[5]/div[3]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/ul")
    epi=[]
    for i in episodes: 
        url=i.xpath(r"li/a")[0].attrib["href"]
        pagetype,indexurl=getIndexPage(url)
        #print i.xpath(r"li/a")[0].attrib["href"]
        #print indexurl
        epi.append(crawlKeywordPage(indexurl))
    return [showIndex,epi]
    #return showIndex
def crawlPage(link):
    output=[]
    for i in link:
        try:
            pageType,indexUrl=getIndexPage(i)
        except:
            continue
        if pageType==0:
            output.append(crawlShowPage(i,indexUrl))
        elif pageType==1:
            output.append(crawlKeywordPage(indexUrl))
        elif pageType==2:
            output.append(sel.getJSON(indexUrl))
    return output
