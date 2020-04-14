#!/usr/local/bin/python3
import requests
import sys
from bs4 import BeautifulSoup

siteIP = str(sys.argv[1])
req_ = requests.get("http://"+siteIP)
print(req_)
print("\n")

print(req_.headers)
print("\n")

soup = BeautifulSoup(req_.text, 'html.parser')

print(soup.title)
print("\n")

home_ = requests.get("http://"+siteIP)
soup = BeautifulSoup(home_.content,"html.parser")

links = soup.find_all("a",href=True)
links_href = []

for link in links:
    links_href.append(link['href'])

links_set = set(links_href)

for link in links_set:
    print(link)
