from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import re
driver = webdriver.Firefox()
prog=re.compile(r"var youkuData = eval.*;")

def getPage(link):
    # try to get page
    tried=0
    driver.get(link)
    script=driver.find_elements_by_xpath("/html/body/script[10]")
    while len(script)==0:
        tried+=1  
        driver.get(link)
        script=driver.find_elements_by_xpath("/html/body/script[10]")
        if tried >5:
            raise Exception("No Index for this page")
    return driver.page_source
    
def getJSON(link):
    try:
        html=getPage(link)
    except:
        return {'url':link}
    JSON=prog.search(html).group(0)[27:-8]
    temp = eval(JSON)
    temp['url']=link
    return temp
