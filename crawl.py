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
import re

# -*- coding: utf-8 -*-
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import copy
import os
 
# 体彩 排列5
URL = "https://www.cnblogs.com/huangxie/"
page = urlopen(URL)
#soup = BeautifulSoup(page,"lxml")
bsObj = BeautifulSoup(page.read(),"lxml")

crawl_content = bsObj.find("div",{"class":"forFlow"})

sub_htmls = crawl_content.find_all("div",{"class":"c_b_p_desc"})

def GetCss(html):
#    patterncss ='<link[]type="text/css"  href="(.*?)"'
    patterncss = r'\.css'
#    patternjs = '<script src="(.*?)"'
#    patternimg = '<img src="(.*?)"'
#    patternpage = '<a.*?href="(.*?)"'
#    patternonclick = "openQuestion.*?'(.*?)'"
    href = re.compile(patterncss, re.S).findall(html)
#    href += re.compile(patternimg, re.S).findall(html)
#    href += re.compile(patternpage, re.S).findall(html)
#    href += re.compile(patternjs, re.S).findall(html)
#    href += re.compile(patternonclick, re.S).findall(html)
    return href


def CreateFolder(path):
	folder = os.path.exists(path)
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print("Folder "+path+" created")
	else:
		print(path+"already existed")
        
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

def SaveSubHtmls(sub_html_list):
    for link in sub_htmls: 
        sub_url = link.find("a").get("href")
        sub_page = urlopen(sub_url)
        #print(sub_url)   
        bsObj = BeautifulSoup(sub_page.read(),"lxml")
        print(GetCss(bsObj.prettify()))
        
        sub_file_name = validateTitle(bsObj.find("head").find("title").text+".html")
        sub_folder_name = validateTitle(bsObj.find("head").find("title").text+"_files")
        CreateFolder(sub_folder_name)
        
        print(sub_file_name)
        f = open(sub_file_name, "w",encoding='UTF-8')  
        f.write(bsObj.prettify())
       

print(sub_htmls)
SaveSubHtmls(sub_htmls)