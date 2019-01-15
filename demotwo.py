# -*- coding: UTF-8 -*-
"""
 获取向北向北的日记
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


# 获得指定开始url
def get_url(root_url,start):
    return root_url+"?start="+str(start)+"&type=note"

def get_review(page_url):
    movies_list=[]
    response=requests.get(page_url)
    soup=BeautifulSoup(response.text,"lxml")
    # 找到ol ol的class是grid_view
    soup=soup.find_all(name='div',attrs={"class":"note"})
    for items in soup:
            print items.text
            print "***********************"
           
    

if __name__ == "__main__":
    root_url="https://www.douban.com/people/2650429/notes"
    start=0
    # while适用于很多页
    while(start<70):
        movies_list=get_review(get_url(root_url,start))
       
        start+=10


    