# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 10:32:49 2018

@author: westine
"""
from pylab import plt
plt.style.use('seaborn')
import matplotlib as mpl
mpl.rcParams['font.family'] = 'serif'
import warnings; warnings.simplefilter('ignore')
V0 = 17.6639
r = 0.01
import pandas as pd


# -*- coding: utf-8 -*-
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import copy
 
# 体彩 排列5
URL = "https://www.cnblogs.com/huangxie/"
page = urlopen(URL)
#soup = BeautifulSoup(page,"lxml")
bsObj = BeautifulSoup(page.read(),"lxml")

crawl_content = bsObj.find("div",{"class":"forFlow"})

sub_htmls = crawl_content.find_all("div",{"class":"c_b_p_desc"})


for link in sub_htmls: 
    sub_url = link.find("a").get("href")
    sub_page = urlopen(sub_url)
    print(sub_url)
    
    bsObj = BeautifulSoup(sub_page.read(),"lxml")
    f = open(sub_url, "w",encoding='UTF-8')  
    f.write(bsObj.prettify())
   



