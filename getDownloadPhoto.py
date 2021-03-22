import re
import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http://uC8ADg1n:wWwVs3jr@194.156.105.80:51606',
    'https': 'http://uC8ADg1n:wWwVs3jr@194.156.105.80:51606',
}

site = 'https://www.rockpapershotgun.com/pubg-guns-weapons-update-6-2-pubg-gun-stats-best-weapons-in-season-6'

response = requests.get(site, proxies=proxies)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png|svg))$', url)
    if not filename:
         print("Linkul nu este disponibil: {}".format(url))
         continue
    with open(filename.group(1), 'wb') as f:
        if 'https' not in url:
            url = '{}{}'.format(site, url)
        response = requests.get(url, proxies=proxies)
        f.write(response.content)