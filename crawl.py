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

def getSubHtmls(sub_htmls):
    for link in sub_htmls: 
        sub_url = link.find("a").get("href")
        sub_page = urlopen(sub_url)
        print(sub_url)   
        bsObj = BeautifulSoup(sub_page.read(),"lxml")
        sub_file_name = sub_url.replace("://","_").replace("/","_")
        f = open(sub_file_name, "w",encoding='UTF-8')  
        f.write(bsObj.prettify())
       


import os
from bs4 import BeautifulSoup 
import re
siteUrls = " "
 
url = "http://www.sina.com.cn"
fileNames = re.findall(r'/[^\?]*\?([^/|^\?]*)$',url)
def getContent(url):
	content = urlopen(url).read()
	content = writeCss(url,content)
	content = writefileName(url,content)
	fileNames = re.findall(r'/[^\?]*\?([^/|^\?]*)$',url)
	fileName = fileNames[0]
	print(fileName)
	f = file(fileName+".html",'w')
	f.write(content)
	f.close()
 
def writeCss(url,content):
    soup = BeautifulSoup(content)
    print(soup.prettify())
    csss = soup.findAll('link',attrs={'type':'text/css'})
    css_pat = re.compile('.*/(.*)\.css')
    fileNames = re.findall(r'/[^\?]*\?([^/|^\?]*)$',url)
    fileName = fileNames[0]
    print(fileName)
    for css in csss:
    	cssnames = re.findall(r'.*/(.*)\.css',str(css))
    	cssurls = re.findall(r'.*href=\"([^\"]*)\"',str(css))
    	print(cssnames[0])
    	print(cssurls[0])
    	cssurl = "http://review.artintern.net/" + cssurls[0]
    	print(cssurl)
    	content = content.replace(cssurls[0],fileName + "/" + cssnames[0]+".css")
    	print(os.path.isdir(fileName))
    	if not os.path.isdir(fileName):
    		os.mkdir(fileName)
    	csscontent = urllib2.urlopen(cssurl).read()
    	cssNewName = fileName+"/"+cssnames[0]+".css"
    	cssfile = file(cssNewName,'w')
    	cssfile.write(csscontent)
    	cssfile.close()
    return content
 
def writefileName(url,content):
	soup = BeautifulSoup(content)
	imgs = soup.findAll('img')
	img_pat = re.compile('.*/(.*)\.[jpg|gif]')
	fileNames = re.findall(r'/[^\?]*\?([^/|^\?]*)$',url)
	fileName = fileNames[0]
	for img in imgs:
		imgNames = re.findall(r'.*/(.*)\.[jpg|gif]',str(img))
		imgType = re.findall(r'.*/.*\.([^ ]*)"',str(img))
		imgUrls = re.findall(r'.*src=\"([^\"]*)\"',str(img))
#		print imgNames[0]
#		print imgType[0]
#		print imgUrls[0]
		imgUrl = "http://review.artintern.net/" + imgUrls[0]
#		print imgUrl
		content = content.replace(imgUrls[0],fileName+"/"+imgNames[0]+"."+imgType[0])
		if not os.path.isdir(fileName):
			os.mkdir(fileName)
		imgContent = urllib2.urlopen(imgUrl).read()
		imgNewName = fileName+"/"+imgNames[0]+"."+imgType[0]
		imgfile = file(imgNewName,'w')
		imgfile.write(imgContent)
		imgfile.close()
	return content
 
getContent(url)


