import re
showPage=re.compile(r"http://www.youku.com/show_page/(.*)")
keywordPage=re.compile(r"http://v.youku.com/v_show/(.*)")
indexPage=re.compile(r"http://index.youku.com/(.*)")
def getIndexPage (url):
    m=showPage.match(url)
    if m:
        return r"http://index.youku.com/vr_show/show"+m.group(1)
    m=keywordPage.search(url)
    if m:
        return r"http://index.youku.com/vr_keyword/id_"+m.group(0)
    m=indexPage.search(url)
    if m:
        return url
    raise Exception("Non-youku page")
    
