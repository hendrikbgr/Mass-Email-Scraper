import requests
from bs4 import BeautifulSoup
import random
from fake_useragent import UserAgent
import user_agent
import re
import time
import json
import csv

import config

emails = []
counter = 0
cookies = {"CONSENT": "YES+cb.20210720-07-p0.en+FX+410"}

print(config.site_list)

for sitep in config.site_list:
    for emailp in config.email_list:
        for keyword in config.keyword_list:
            r = requests.Session()
            headers = user_agent.generate_navigator(os=None, navigator=None, platform=None, device_type=None)
            r.headers = headers
            proxy_picker = random.choice(config.proxy_list)
            proxies = {
            "http": f"http://{proxy_picker}",
            "https": f"http://{proxy_picker}",
            }
            print()
            print(f'Request for: {keyword} | Site: {sitep} | Provider: {emailp} | Proxy: {proxy_picker}')
            url = f'https://www.google.com/search?q={keyword}+"%40{emailp}"+site%3A{sitep}&tbm=nws&lr=lang_en&hl=en&sort=date&num=100'
            res = r.get(url, headers=headers, cookies=cookies, proxies=proxies)
            soup = BeautifulSoup(res.text, "html.parser")
            captcha = soup.find_all("form", id="captcha-form")
            heading_object=soup.find_all("div", class_="kCrYT")

            # Iterate through the object 
            # and print it as a string.
            if not captcha:
                for info in heading_object:
                    text = str(info.getText())
                    #text = "asdas sdasd kaylascanna@gmail.com asda asdas"
                    match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
                    if not match:
                        print(f'Keyword: {keyword} | Site: {sitep} | No Result!')
                        pass
                    else:
                        counter += 1
                        print(f'Keyword: {keyword} | Email: {match[0]} | Site: {sitep} | Found: {counter}')
                        emails.append(match[0])
                        csv_data = f'{keyword},{match[0]},{sitep}'
                        with open('data.csv','a', encoding="utf-8") as fd:
                            fd.write(csv_data + "\n")
            else:
                print(f'{proxy_picker} blocked by Captcha!')

with open('data.txt', 'w') as f:
    for item in emails:
        f.write("%s\n" % item)