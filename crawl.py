import pickle
import crawlPage

f=open('link','r')
link=pickle.load(f)
f.close()

data=crawlPage.crawlPage(link[1][1:10])
