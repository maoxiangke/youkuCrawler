from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import re
driver = webdriver.Firefox()
prog=re.compile(r"var youkuData = eval.*;")

def getPage(link):
    # try to get page
    driver.get(link)
    script=driver.find_elements_by_xpath("/html/body/script[10]")
    if len(script)==0:
        driver.get(link)
        script=driver.find_elements_by_xpath("/html/body/script[10]")

    return driver.page_source
    
def getJSON(link):
    html=getPage(link)
    JSON=prog.search(html).group(0)[27:-8]
    temp = eval(JSON)
    temp['url']=link
    return temp
