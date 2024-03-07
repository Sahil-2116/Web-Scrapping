#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[43]:


# connect to website
URL = 'https://www.amazon.ca/Funny-Systems-Business-Analyst-T-Shirt/dp/B0B63BYBQB/ref=sr_1_2?crid=W3EN2D5E00Z4&dib=eyJ2IjoiMSJ9.2bnpDYVNwrP3hgwJOFbJETF82Cysgo6K8iY5CoqrryKLILDxJ1MyGp7ZiqQRocj_k6eKQLUBKvyR5Gdwyx9FYB1VXGawe3qvF_bLFCktQNWqIkrbqwl3QL54X4hMOCe9y8soVixTFic6kin2QofwAuyXMHEMn2P325ig7uBnCPVGCWewUDgk_cex3Os3f2o8-Qe5XXMYbePxTv2jTJ5svYot6IoiUnbPHD3wGpniiUbrlv9KLlaa42ghRP3FHvMDhl33BVhkROLE9tXg58IflTyBXvg_MtjTSJXeJLD6Gek.T3X7n-ervSofGAyJD6DcRWf5GCo6XJ4G5Z7AyFR3YB4&dib_tag=se&keywords=data%2Banalyst%2Btshirt&qid=1709791474&sprefix=%2Caps%2C161&sr=8-2'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='title').get_text()

price = soup2.find("span", attrs={"class":'a-price aok-align-center'}).find("span", attrs={"class":'a-offscreen'}).get_text()


print(title)
print(price)



# In[44]:


price = price.strip()[1:]
title = title.strip()

print(price)
print(title)


# In[53]:


import datetime

today = datetime.date.today()

print(today)



# In[54]:


import csv

header = ['Product_Title', 'Price', 'Date']
data = [title, price, today]

with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    


# In[66]:


import pandas as pd

df = pd.read_csv(r'/Users/sahildabgotra/Desktop/AmazonWebScraperDataset.csv')

print(df)
                 


# In[65]:


# appending data to csv file

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[70]:


def check_price():
    URL = 'https://www.amazon.ca/Funny-Systems-Business-Analyst-T-Shirt/dp/B0B63BYBQB/ref=sr_1_2?crid=W3EN2D5E00Z4&dib=eyJ2IjoiMSJ9.2bnpDYVNwrP3hgwJOFbJETF82Cysgo6K8iY5CoqrryKLILDxJ1MyGp7ZiqQRocj_k6eKQLUBKvyR5Gdwyx9FYB1VXGawe3qvF_bLFCktQNWqIkrbqwl3QL54X4hMOCe9y8soVixTFic6kin2QofwAuyXMHEMn2P325ig7uBnCPVGCWewUDgk_cex3Os3f2o8-Qe5XXMYbePxTv2jTJ5svYot6IoiUnbPHD3wGpniiUbrlv9KLlaa42ghRP3FHvMDhl33BVhkROLE9tXg58IflTyBXvg_MtjTSJXeJLD6Gek.T3X7n-ervSofGAyJD6DcRWf5GCo6XJ4G5Z7AyFR3YB4&dib_tag=se&keywords=data%2Banalyst%2Btshirt&qid=1709791474&sprefix=%2Caps%2C161&sr=8-2'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='title').get_text()

    price = soup2.find("span", attrs={"class":'a-price aok-align-center'}).find("span", attrs={"class":'a-offscreen'}).get_text()
    
    price = price.strip()[1:]
    title = title.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    
    


# In[73]:


while(True):
    check_price()
    time.sleep(86400)


# In[72]:


import pandas as pd

df = pd.read_csv(r'/Users/sahildabgotra/Desktop/AmazonWebScraperDataset.csv')

print(df)


# In[ ]:





# In[ ]:




