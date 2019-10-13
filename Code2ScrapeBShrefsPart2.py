# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:23:20 2017

@author: User
"""

from bs4 import BeautifulSoup, SoupStrainer
import time
import requests

allURL = []

with open("BShrefs2a.txt",'r') as feedFile:
    allURL = feedFile.read().splitlines()   #open doc & feed into list
    
while len(allURL) > 0:
    url = allURL[0]      #feed the first url to the code for scraping
    blogPostHref = []
    rejURLs = []
    
    time.sleep(1)
    
    r = requests.get(url)
    contents = SoupStrainer("h3", {"class": "post-title entry-title"})
    soup = BeautifulSoup(r.content, "lxml", parse_only = contents)
    
   
    for link in soup.find_all ("a", href=True): 
        print (link['href'])
        blogPostHref.append(link['href'])  #and adds it to the href list

    else:
        rejURLs.append(url)
        
    if len(blogPostHref) >= 1:
        for i in (blogPostHref):
            with open ("BShrefs2a3.txt", "a") as outfile:
                outfile.write(i + '\n')
    else:
        for i in (rejURLs):
            with open ("BShrefs2a3Fail.txt", "a") as outfile:
                outfile.write(url + "\n")
                
    del allURL[0] #delete the starting url
        
    print(allURL)