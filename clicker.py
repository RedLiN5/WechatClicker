import requests
from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import etree
import re
import time
import datetime
import pandas as pd
import numpy as np
import glob
import os


url = "https://mp.weixin.qq.com/s?__biz=MzA3OTIzNDM2NA==&mid=2650623924&idx=1&sn=7ec2d25f373d173079950875c09abb9d&mpshare=1&scene=1&srcid=0824zwiKu2OuVt5WH1bQJOIf&key=c4c5bf741ef7e272fac5a83a331538f9fdc5690f5fda7324de297dcd3f977945a1171bd92807cab76784a95baa2a79a8c926d9bf7ee1fb5a775966c9e7c28b9e8ac03da8246afab14901f11592823ce5&ascene=0&uin=MTIyODAyNDE4MA%3D%3D&devicetype=iMac+MacBookPro11%2C3+OSX+OSX+10.12.1+build(16B2555)&version=12010210&nettype=WIFI&fontScale=100&pass_ticket=ax8%2Bp78Sf3NHqBI2s9KK3oq4YeFOtsB4T2ZQnkyle4UnWcGSAao6wmnky%2Bv89Ern"
session = requests.Session()
r = session.post(url)