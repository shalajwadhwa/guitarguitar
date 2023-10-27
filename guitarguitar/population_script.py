# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guitarguitar.settings')
# import django
# django.setup()

import json
import requests
from bs4 import BeautifulSoup


## Scrape the data from the given urls
def scrape_info(url):
    res = requests.get(url)
    res_json = json.loads(res.text)
    print(res_json)
        

scrape_info("https://www.guitarguitar.co.uk/hackathon/customers/")