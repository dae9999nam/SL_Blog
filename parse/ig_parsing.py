import csv
from bs4 import BeautifulSoup
import requests

#Read CSV

csv_file_path = r''

with open(csv_file_path, 'r') as f:
    reader = csv.reader(f)
    next(reader) #skip the header row
    for row in reader:
        name, url = row

        #Make a request to the Instagram profile URL
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        #Extract the follwer count from the meta tag
        meta_tag = soup.find('meta', property='og:description')

        if meta_tag:
            description = meta_tag['content']
            follower_count = None
        
            #Extract the follwer count from the description using 
            if '팔로워' in description:
                start_index = description.index('팔로워') + len()
                end_index = description.index('명', start_index)
                follower_count_str = description[start_index:end_index]
                follower_count = int(follower_count_str.replace(',', ''))

            print(f"{name}: Follower count = {follower_count}")

        else:
            print(f"{name}: Follower count not found.")