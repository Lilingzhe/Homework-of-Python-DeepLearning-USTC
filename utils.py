#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import json
import re
import logging

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

def get_neuron_name(soup):
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
    ulist = ulist[1:]    
    return ulist

def get_img_link(ulist):
    img_link = "http://neuromorpho.org/images/imageFiles/" + ulist[3][1] + "/" + name + ".png"
    return img_link

def dl_img(img_link,name,path):
    #download image in certain path
    response = requests.get(img_link)
    img = response.content
    if response.status_code == 200:
        open(path + name + ".png" ,'wb').write(img)
    del response    


    