# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:18:54 2017

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:25:15 2017

@author: User
"""

from bs4 import BeautifulSoup, SoupStrainer
import requests
import pandas as pd
import time

allURL = []

with open("BShrefs2a3.txt",'r') as feedFile:
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
        contents = SoupStrainer(id = "main")
        soup = BeautifulSoup(r.content, "lxml", parse_only = contents)
        
        g_data = soup.find_all("h3", {"class": "post-title entry-title"})
        if g_data:
           for item in g_data:
               blogPostTitle.append(item.text)
        else:
            blogPostTitle.append('No Title')
        
        h_data = soup.find_all("h2", {"class": "date-header"})
        if h_data:    
            for item in h_data:
                blogPostDate.append(item.text)
        else:
            blogPostDate.append('No Date')
      
        j_data = soup.find_all("div", {"class": "post-body entry-content"})
        if j_data:
            for item in j_data:
                blogPostContent.append(item.text)
        else:
            print('No Content')
        
   
    scrape_data()
   
    #if len(blogPostTitle) == len(blogPostDate) == len(blogPostContent): #checks to see if your lists are of equal length...
    if ('2017') in blogPageURL:
        
        df = pd.DataFrame({'id': blogPageURL, 'PubDate': blogPostDate[0], 'Title': blogPostTitle[0], 'Content': blogPostContent}) #create a spreadsheet...
        df.to_csv('BSblogs2017.csv', mode = 'a', header = False)#...and append your data.
        blogPostTitle = []
        blogPostDate = []
        blogPostContent = []
        blogPageURL = []
        del allURL[0]
    else:
        #with open ("BSblogs2017Fail.txt", 'a') as outfile:
            #outfile.write(url + "\n")
        print('2016')
        del allURL[0]  

    print(allURL) #just to let you know it's finished.
    