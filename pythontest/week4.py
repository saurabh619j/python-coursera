# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup 

URL = input("Enter the URL:") #Enter main URL
link_line = int(input("Enter position:")) - 1 #The position of link relative to first link
count = int(input("Enter count:")) #The number of times to be repeated

while count >= 0:
    html = urllib.request.urlopen(URL).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print(URL)
    URL = tags[link_line].get("href", None)
    count = count - 1