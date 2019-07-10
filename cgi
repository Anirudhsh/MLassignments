#!/usr/bin/python3

import cgi
import cgitb # to show Common error in web browser cgiTraceBack

from googlesearch import search

cgitb.enable()

print("Content-type:text/html")
print("")

webdata = cgi.FieldStorage() #This will collect all the HTML code with data

#Now Extracting Value of x

mymood = webdata.getvalue('mood')
mysonglist=[]

for url in googlesearch.search_videos("heavy metal",stop=10):

    mysonglist.append(url)

songnum = numpy.random.random_integers(1,10)

print(songnum)

print(mysonglist[songnum])
