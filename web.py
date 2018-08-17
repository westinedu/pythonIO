# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:31:51 2018

@author: westine
"""
from pylab import plt

import matplotlib as mpl

import warnings; warnings.simplefilter('ignore')

import pandas as pd
#h5 = pd.HDFStore('./source/vstoxx_data_31032014.h5', 'r')
#futures_data = h5['futures_data']  # VSTOXX futures data
#options_data = h5['options_data']  # VSTOXX call option data
#h5.close()

import datetime as dt




# -*- coding: utf-8 -*-
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import copy
 
# 体彩 排列5
URL = "https://www.thiswaytocpa.com/licensure/state-requirements/"
page = urlopen(URL)
#soup = BeautifulSoup(page,"lxml")
bsObj = BeautifulSoup(page.read(),"lxml")
#statetable = bsObj.findAll("table")

count = 0
for child in bsObj.find("table",{"class":"state-req-table"}).children:
    count += 1
    print("This is state",count)
    print(child)

print(bsObj.find("table",{"class":"state-req-table"}).prettify()) 
state_table = bsObj.find("table",{"class":"state-req-table"})    

f = open("AICPA.html", "w",encoding='UTF-8')  
f.write(state_table.prettify())

print(state_table.find("thead").tr)
newtag = copy.copy(state_table.find("th",{"class":"state-req-intl"}))
print(newtag.prettify())
newtag['class']="Education Requirement for Licensure"

#newtag['span']="Education Requirement for Licensure"
#del newtag['span']

print(newtag.find("span").string )
newtag.find("span").string = "Education Requirement for Licensure"
print(state_table.find("thead").tr)
state_table.find("thead").tr.append(newtag)

newtag1 = copy.copy(state_table.find("th",{"class":"state-req-intl"}))
newtag1['class']="Hours in Accounting"
newtag1.find("span").string = "Hours in Accounting"
print(newtag1.prettify())
state_table.find("thead").tr.append(newtag1)

newtag2 = copy.copy(state_table.find("th",{"class":"state-req-intl"}))
newtag2['class']="Experience Requirements"
newtag2.find("span").string = "Experience Requirements:"

state_table.find("thead").tr.append(newtag2)

print(state_table.find("thead").tr)


print(state_table.find("thead").tr.prettify())
f.write(state_table.prettify())
#for child in state_table.find("thead").tr.children:
#    print(child)


#获取内链接，并且拼成url
addressList = list()
from urllib.parse import urljoin  
for link in state_table.find_all('a'): 
    print(link.get('href'))
    ipAddress = urljoin(URL,link.get('href'))
    addressList.append(ipAddress)
    
print(addressList)
#count = 0
#for address in addressList:
#    if count == 0:
#        print(address.title())
#        count += 1
#        html = urlopen(address)
#        bsObj = BeautifulSoup(html.read(),"lxml")
#        print(bsObj)
#        print(bsObj.find("table",{"id":"requirements_table","class":"table table-bordered"})) 
##        print(bsObj.find("table",{"id":"requirements_table"}).find("h3",{"id":"page_title","class":"teal-accent-light-text"})) 
##    

state_table_trs = state_table.find_all(name='tr')

print(state_table_trs[0])


html = urlopen(addressList[0])
bsObj = BeautifulSoup(html.read(),"lxml")
print(bsObj.find("h1",{"id":"page_title","class":"teal-accent-light-text"}).text)
sub_table=bsObj.find("table",{"id":"requirements_table","class":"table table-bordered"})
trs = sub_table.find_all(name='tr')
count = 1
for address in addressList:
    html = urlopen(address)
    bsObj = BeautifulSoup(html.read(),"lxml")
    print(bsObj.find("h1",{"id":"page_title","class":"teal-accent-light-text"}).text)
    sub_table=bsObj.find("table",{"id":"requirements_table","class":"table table-bordered"})
    trs = sub_table.find_all(name='tr')
  # tds=trs[6].find_all(name='td')
    temp_newtag = copy.copy(newtag)
    temp_newtag.find("span").string = trs[4].find_all(name='td')[1].text
    print(trs[4])
    temp_newtag1 = copy.copy(newtag1)
    temp_newtag1.find("span").string = trs[6].find_all(name='td')[1].text
    
    temp_newtag2 = copy.copy(newtag2)
    temp_newtag2.find("span").string = trs[8].find_all(name='td')[1].text
    
    state_table_trs[count].append(temp_newtag)
    state_table_trs[count].append(temp_newtag1)
    state_table_trs[count].append(temp_newtag2)
    count += 1
    
    

#print(trs[4].find_all(name='td')[1].text)





#state_table_trs[1].append(newtag)
#state_table_trs[1].append(newtag1)

#state_table_trs[1].append(copy.copy(newtag))
print(state_table_trs[1])

f.write(state_table.prettify())



#try:
#    html = urlopen(URL)
#except HTTPError as e:  
#    print(e)
## 返回空值，中断程序，或者执行另一个方案
#else:
## 程序继续。注意：如果你已经在上面异常捕捉那一段代码里返回或中断（break），
## 那么就不需要使用else语句了，这段代码也不会执行 
#    bsObj = BeautifulSoup(html.read(),"lxml")
#    print(bsObj.html)
#    
    


#fp = open("pl5.txt","w")
#tables = soup.findAll('table')
#tab = tables[0]
#for tr in tab.tbody.findAll('tr'):
#    for td in tr.findAll('td'):
#        text = td.getText().encode('cp936')+'!'
#        print(text)
#        fp.write(text)
#    fp.write('\n')
##
#fp.close()