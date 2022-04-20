#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import json
import re
import logging
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class  Neuron:
    def __init__(self,name,pic,details):
        self.name = name
        self.pic = []
        self.details = {}
        
    def save_neuron(self):
        return()
    

def get_links(soup):
    #get link of every neuron
    links = []
    for link in soup.find_all('a'):
        #print(link.get('href'))
        if(link.get('href')):
            links.append(link.get('href'))
    return links

def get_os_from_link(link):
    neuron_link = "http://neuromorpho.org/" + link
    logging.captureWarnings(True)
    Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    req = requests.get(neuron_link,headers=Headers,verify=False)
    soup = BeautifulSoup(req.text,'html.parser')
    return soup

def get_neuron_name(soup,link):
    #get neuron_name
    info = soup.find_all("div",class_="info")
    name = link[28:]
    return name

def get_neuron_details(soup):
    #get neuron_details
    trs = soup.find_all('tr')
    ulist = []
    for tr in trs:
        ui = []
        for td in tr:
            if(td != '\n' and td.string):
                s = td.string
                s = re.sub('\s',' ',s)
                ui.append(s)
        if(ui):
            ulist.append(ui)
    details = ulist[1:]  
    return details

def get_img_link(ulist,name):
    img_link = "http://neuromorpho.org/images/imageFiles/" + ulist[3][1] + "/" + name + ".png"
    return img_link

def dl_img(img_link,name,path):
    #download image in certain path
    logging.captureWarnings(True)
    Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    response = requests.get(img_link,headers = Headers, verify = False)
    img = response.content
    if response.status_code == 200:
        open(path + name + ".png" ,'wb').write(img)
    del response    

def read_img(path,name):
    img = mpimg.imread(path+name+'.png')
    # plt.imshow(img)
    # plt.show()
    return img
    
#converse output(str) to list
import cv2

def read_details_info(txt_file):
    #read from txt
    f = open(txt_file,'r')
    lists = []
    name_list = []
    while(True):
        line = f.readline()
        if line:
            list = line.split('[')
            new_list = []
            info = ''
            for i in list:
                i = i.strip("[',] ")
                i = i.strip("',")
                i = i.replace("', '","")
                if(i!=' ' and i and i!='\n'):
                    new_list.append(i)
                    info = info + i + '\n'
            name = new_list[2][13:]
            name_list.append(name)
            fname = name + '.txt'
            file = open(fname,'w')
            file.write(info)
            file.close
            lists.append(new_list)
        else:
            break
    return lists,name_list    
