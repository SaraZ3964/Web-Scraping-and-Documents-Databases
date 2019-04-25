#!/usr/bin/env python
# coding: utf-8

# In[6]:


from bs4 import BeautifulSoup
from splinter import Browser
executable_path = {"executable_path": "\Users\saraz"}
browser = Browser("chrome", **executable_path, headless=False)


# In[7]:


url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[8]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[9]:


article = soup.find("div", class_="list_text")
news_p = article.find("div", class_="article_teaser_body").text
news_title = article.find("div", class_="content_title").text
news_date = article.find("div", class_="list_date").text
print(news_date)
print(news_title)
print(news_p)


# In[10]:


url2 = "https://jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url2)


# In[11]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
image = soup.find("img", class_="thumb")["src"]
img_url = "https://jpl.nasa.gov"+image
featured_image_url = img_url


# In[12]:


import requests
import shutil
response = requests.get(img_url, stream=True)
with open('img.jpg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)


# In[13]:


from IPython.display import Image
Image(url='img.jpg')

