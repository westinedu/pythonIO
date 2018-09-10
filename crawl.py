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
import logging
# -*- coding: utf-8 -*-
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import copy
import os
import time
 
# 体彩 排列5
URL = "https://www.cnblogs.com/huangxie/"
page = urlopen(URL)
#soup = BeautifulSoup(page,"lxml")
bsObj = BeautifulSoup(page.read(),"lxml")

crawl_content = bsObj.find("div",{"class":"forFlow"})

sub_htmls = crawl_content.find_all("div",{"class":"c_b_p_desc"})


def initLogging(logFilename):
  """Init for logging
  """
  logging.basicConfig(
                    level    = logging.DEBUG,
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    datefmt  = '%y-%m-%d %H:%M',
                    filename = logFilename,
                    filemode = 'w');
  console = logging.StreamHandler()
  console.setLevel(logging.INFO)
  formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
  console.setFormatter(formatter)
  logging.getLogger('').addHandler(console)

def GetCss(soup_html):
#    patterncss =r'<link\wtype="text/css"\whref="(.*?)"'
    #patterncss = r'\.css'
#    patternjs = '<script src="(.*?)"'
#    patternimg = '<img src="(.*?)"'
#    patternpage = '<a.*?href="(.*?)"'
#    patternonclick = "openQuestion.*?'(.*?)'"
#    href = re.compile(patterncss, re.S).findall(html)
#    href += re.compile(patternimg, re.S).findall(html)
#    href += re.compile(patternpage, re.S).findall(html)
#    href += re.compile(patternjs, re.S).findall(html)
#    href += re.compile(patternonclick, re.S).findall(html)
    for k in  soup_html.find_all(href=re.compile("css")):
        print(k.get("href"))

def GetJs(soup_html):
    for k in  soup_html.find_all(src=re.compile("js")):
        print(k.get("src"))

def GetImg(soup_html):
    for k in  soup_html.find_all("img"):
        print(k.get("src"))


def CreateFolder(path):
	folder = os.path.exists(path)
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print("Folder "+path+" created")
	else:
		print(path+" already existed")
        
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
#        print(bsObj.find("head").prettify())
        GetCss(bsObj.find("head"))
        GetJs(bsObj.find("head"))
        GetImg(bsObj)
        logging.info(bsObj.prettify())
        
        sub_file_name = validateTitle(bsObj.find("head").find("title").text+".html")
        sub_folder_name = validateTitle(bsObj.find("head").find("title").text+"_files")
        CreateFolder(sub_folder_name)
        
        print(sub_file_name)
        f = open(sub_file_name, "w",encoding='UTF-8')  
        f.write(bsObj.prettify())
        time.sleep(5)
       
initLogging('test.log')
#print(sub_htmls)
SaveSubHtmls(sub_htmls)