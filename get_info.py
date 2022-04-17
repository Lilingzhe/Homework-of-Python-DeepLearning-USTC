#get_neuron_info

#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import json
import re
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

import logging
from utils import *
get_ipython().run_line_magic('matplotlib', 'inline')

#get list of chimpanzees' neurons
html = "http://neuromorpho.org/byspecies.jsp#top"
#logging.captureWarnings(True)
chimpanzee = "http://neuromorpho.org/getdataforbyspecies.jsp?species=chimpanzee"
logging.captureWarnings(True)
Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
req = requests.get(chimpanzee, headers = Headers,verify=False)
soup = BeautifulSoup(req.text,'html.parser')
#print(soup.prettify())
#save path
path = "C:\\Users\\14119\\Documents\\python&dl\\img\\"

if __name__ == '__main__':
    links = get_links(soup)
    #print(links)
    neurons = []
    #print(links)
    for link in links:
        #get information of each neuron
        #print(link)
        soup_neuron = get_os_from_link(link)
        info = soup.find_all("div",class_="info")
        name = link[28:]
        #print(soup)
        details = get_neuron_details(soup_neuron)
        img_link = "http://neuromorpho.org/images/imageFiles/" + details[3][1] + "/" + name + ".png"
        dl_img(img_link,name,path)
        img = read_img(path,name)
        #save information of neuron
        neuron = Neuron(name,img,details)
        neurons.append(neuron)
    
