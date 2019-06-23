from bs4 import BeautifulSoup
import requests
URL = "https://en.wikipedia.org/wiki/Machine_learning"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib')
sdiv = soup.find("div", {"id": "mw-content-text"})
stext = sdiv.text
words=str(stext).replace("\n"," ")
words=words.split(" ")
wordcnt={}
for i in words:
    if i not in wordcnt:
        wordcnt[i]=1
    else:
        wordcnt[i]+=1
wosorted = sorted(wordcnt.items(), key =lambda x:(x[1], x[0]),reverse=True)
#print(wosorted)
# 0 not taken as it is ''
top20words = wosorted[1:21]
print(top20words)
