# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:09:11 2016

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:23:09 2016

@author: User
"""

from bs4 import BeautifulSoup, SoupStrainer
import requests
import pandas as pd
import time
import re

allURL = []

with open("WPblogHrefs2017c.txt",'r') as feedFile:
    allURL = feedFile.read().splitlines()

while len(allURL) > 0:
    blogPostTitle = []
    blogPostDate = []
    blogPostContent = []
    blogPageURL = []
        
    url = allURL[0]
    blogPageURL = allURL[0]
    
    time.sleep(1)
    
    def scrape_data():
        r = requests.get(url) 
        contents = SoupStrainer(id = "content")
        soup = BeautifulSoup(r.content, "lxml", parse_only =contents)
        
        g_data = soup.find_all("h1", {"class": "entry-title"})
        g1_data = soup.find_all("h2", {"id": re.compile("post -*")})
        g2_data = soup.find_all("h2", {"class": "entry-title"})
        g3_data = soup.find_all("header", {"class": "entry-header"})
        g4_data = soup.find_all("h1")
        g5_data = soup.find_all("h2")
        g6_data = soup.find_all("div", {"class": "posttitle"})
        g6a_data = soup.find_all("div", {"class": "title"})
        g7_data = soup.find_all("header", {"class": "post-title"})
        g8_data = soup.find_all("h2", {"class": "posttitle"})
        g9_data = soup.find_all("h1", {"class": "post-title"})
        
            
        if g_data:  
            for item in g_data:
                blogPostTitle.append(item.text)
        elif g1_data:
            for item in g1_data:
                blogPostTitle.append(item.text)
        elif g2_data:
            for item in g2_data:
                blogPostTitle.append(item.text)
        elif g3_data:
            for item in g3_data:
                blogPostTitle.append(item.text)
        elif g4_data:
            for item in g4_data:
                blogPostTitle.append(item.text)
        elif g5_data:
            for item in g5_data:
                blogPostTitle.append(item.text)
        elif g6_data:
            for item in g6_data:
                blogPostTitle.append(item.text)
        elif g6a_data:
            for item in g6a_data:
                blogPostTitle.append(item.text)        
        elif g7_data:
            for item in g7_data:
                blogPostTitle.append(item.text)
        elif g8_data:
            for item in g8_data:
                blogPostTitle.append(item.text)
        elif g9_data:
            for item in g9_data:
                blogPostTitle.append(item.text)
        else:
            blogPostTitle.append('No Title')
            print ('Done titles!')
                
        h_data = soup.find_all("span", {"class": "entry-date"})
        h1_data = soup.find_all("p", {"class": "post-info"})
        h2_data = soup.find_all("span", {"class": "posted-on"})
        h3_data = soup.find_all("span", {"class": "post-date"})
        h4_data = soup.find_all("header", {"time": "datetime"})
        h5_data = soup.find_all("time", {"class": "entry-date"})
        h6_data = soup.find_all("time")
        h7_data = soup.find_all("time", {"class": "published"})
        h8_data = soup.find_all("p", {"class": "post-date"})
        h9_data = soup.find_all("p", {"class": "the-date"})
        h10_data = soup.find_all("small")
        h11_data = soup.find_all("small", {"class": "date"})
            
        if h_data:    
            for item in h_data:
                blogPostDate.append(item.text)    
        elif h2_data:
             for item in h2_data:
                 blogPostDate.append(item.text)
        elif h3_data:
            for item in h3_data:
                blogPostDate.append(item.text)
        elif h4_data:
            for item in h4_data:
                blogPostDate.append(item.text)
        elif h5_data:
            for item in h5_data:
                blogPostDate.append(item.text)
        elif h6_data:
            for item in h6_data:
                blogPostDate.append(item.text)
        elif h7_data:
           for item in h7_data:
                blogPostDate.append(item.text)
        elif h1_data:
           for item in h1_data:
                blogPostDate.append(item.text)
        elif h8_data:
           for item in h8_data:
                blogPostDate.append(item.text)
        elif h9_data:
           for item in h9_data:
                blogPostDate.append(item.text)
        elif h10_data:
           for item in h10_data:
                blogPostDate.append(item.text)
        elif h11_data:
           for item in h11_data:
                blogPostDate.append(item.text)
        else:
            blogPostDate.append('No date')
            print ('Done dates!')
                                   
        j_data = soup.find_all("div", {"class": "entry-content"})
        j1_data = soup.find_all("div", {"class": "entrytext"})
        j2_data = soup.find_all("div", {"class": "content"})
        j3_data = soup.find_all("div", {"class": "entry-summary"})
        j4_data = soup.find_all("div", {"class": "entry clearfix"})
        j5_data = soup.find_all("div", {"class": "entry"})
        j6_data = soup.find_all("div", {"class": "post-wrap"})
        j7_data = soup.find_all("div", {"class": "post-entry"})
        
        
        if j_data:    
            for item in j_data:
                blogPostContent.append(item.text)
        elif j1_data:
            for item in j1_data:
                blogPostContent.append(item.text)
        elif j2_data:
            for item in j2_data:
                blogPostContent.append(item.text)
        elif j3_data:
            for item in j3_data:
                blogPostContent.append(item.text)
        elif j4_data:
            for item in j4_data:
                blogPostContent.append(item.text)
        elif j5_data:
            for item in j5_data:
                blogPostContent.append(item.text)
        elif j6_data:
            for item in j6_data:
                blogPostContent.append(item.text)
        elif j7_data:
            for item in j7_data:
                blogPostContent.append(item.text)
        else:
            #blogPostContent.append('No Content')
            print ('No content!')
            
    

    scrape_data() #calls the test F1 to scrape opening page
    #get_pages() #calls F3 which includes F2
    
    #if len(blogPostTitle) == len(blogPostDate) == len(blogPostContent):
    df = pd.DataFrame({'id': blogPageURL, 'PubDate': blogPostDate[0], 'Title': blogPostTitle[0], 'Content': blogPostContent})
    df.to_csv('WPblogPosts2017c.csv', mode = 'a', header = False)
    blogPostTitle = []
    blogPostDate = []
    blogPostContent = []
    blogPageURL = []
    del allURL[0]
#    else:
#        with open ("failed2passWPhrefList2008a.txt", 'a') as outfile:
#            outfile.write(url + "\n")
#            print('Done!')
#            del allURL[0]
    print(allURL)      
            
