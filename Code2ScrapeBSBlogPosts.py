# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:49:00 2017

@author: User
"""

import requests
from bs4 import BeautifulSoup, SoupStrainer
import time

timeout = time.time() + 60*2

blogPostHref = []
allURL = []

#url = 'http://videoformyclassroom.blogspot.com/'

with open("BSList.txt",'r') as feedFile:
    allURL = feedFile.read().splitlines()

url = allURL[0]

blogPostHref.append(url)

#while len(allURL) > 0:
#    url = allURL[0]      #feed the first url to the code for scraping
#    blogPostHref = []
    #rejURLs = []
    
    #time.sleep(1)
        
while True:
    time.sleep(1)
    
    while len (allURL) > 0:
       #url = allURL[0]
       #blogPostHref = []
       
        r = requests.get(url)  #use the first URL in the first list
        contents = SoupStrainer(id = "blog-pager-older-link") #locate this
        soup = BeautifulSoup(r.content, "lxml", parse_only = contents) #scrape this
            
        for link in soup.find_all("a", href=True): #this is the only way to get the href
            print (link['href']) #print the URL
            blogPostHref.append(link['href'])
            url = (link['href']) #always gets the last URL in the list
            blogPostHref.pop()
        if not url or time.time() > timeout:
            break
            del allURL[0]
                
            
        for i in (blogPostHref):
            with open ("BShrefs2atest.txt", "a") as outfile:
                if ('2016') in i:
                    outfile.write(i + '\n')
                elif ('2017') in i:
                    outfile.write(i + '\n')
                blogPostHref = []
        del allURL[0]
    else:
        for i in (blogPostHref):
            with open ("BSHrefs2aFailTest.txt", "a") as outfile:
                outfile.write(i + '\n')
        
 
print (url)           

print (allURL[0])
print (blogPostHref)
print (link['href'])


#         
#        time.sleep(10)
#        
#        del allURL[0]
#        
#        print (allURL)
        
        

#url = "http://bloghomepage.com"
#
#while True:
#    r = requests.get(url)
#    soup = BeautifulSoup(r.text)
#
#    # parse the content you need
#
#    url = soup.find("a", "next-page-link")
#    if not url:
#      break