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

    
