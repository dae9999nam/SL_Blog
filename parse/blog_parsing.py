import csv
from bs4 import BeautifulSoup
import requests

# code needed to be fixed
nset = [n for n in csv.reader(f)]

#Print dataset
print(nset)

#Extract URLs from the dataset
head = nset[0]
data = nset[1:]

for name, url in data:
    print(url)