# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 17:47:14 2017

@author: User
"""

from bs4 import BeautifulSoup, SoupStrainer
import requests
#import pandas as pd
#import re
import time

allURL = []

#blogPostDate = []
#blogPostTitle = []
#blogPostContent = []
#blogPostHref = []

#url = ('https://ajgingell.wordpress.com')

with open("WPlistTest.txt",'r') as feedFile:
    allURL = feedFile.read().splitlines()   #open doc & feed into list

while len(allURL) > 0:
    url = allURL[0]      #feed the first url to the code for scraping
    blogPostHref = []  
    rejURL = []
    
    time.sleep(3)
    
    
    def get_hrefs(): #this fuction scrapes url from the first page
        r = requests.get(url)
        contents = SoupStrainer(rel = "bookmark")
        soup = BeautifulSoup(r.content, "lxml", parse_only = contents)
        
       
        for link in soup.find_all ("a", href=True): 
            print (link['href'])
            blogPostHref.append(link['href'])  #and adds it to the href list
    
        else:
            rejURL.append(url)
                
    length = [0,1] #creates a list which counts with the number of entries in the BlogPostDate list.
    check = 0  # ....which is used to stop the loop.
    number = 2
    
    def scrape(number): #starts scraping at page 2 (there is no page 1)
        url_2 = (url + '/page/' + str(number))
        print(url_2)
        
        time.sleep(1)
        
        r = requests.get(url_2)
        contents = SoupStrainer(rel = "bookmark")
        soup = BeautifulSoup(r.content, "lxml", parse_only = contents)
        
    
        for link in soup.find_all ("a", href=True):  #urls from subsequent pages are 
            print (link['href'])                     #scraped & added to the href list
            blogPostHref.append(link['href'])
    
        else:
            rejURL.append(url_2)
        
        length.append(len(blogPostHref))
        print(length)
        
    def get_pages():
        while length[-1] != length[-2]: 
            global number
            scrape(number) #calls the second function
            number += 1 #adds increments of 1 to the page numbers
        
        
    get_hrefs()
    get_pages()

    if len(blogPostHref) >= 1:
        for i in blogPostHref:
            if ('2019') in i:
                with open ("WPblogHrefs2019.txt", "a") as outfile:
                    outfile.write(i + '\n')                
            elif ('2018') in i:
                with open ("WPblogHrefs2018.txt", "a") as outfile:
                    outfile.write(i + '\n')
    else:
        for i in rejURL:
            with open ("WPblogHrefs2019Fail.txt", "a") as outfile:
                outfile.write(i + '\n')
                
    del allURL[0] #delete the starting url
    blogPostHref = []
        
    print(allURL)


        
print (len(blogPostHref))
print (blogPostHref)

