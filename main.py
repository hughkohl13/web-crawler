from bs4 import BeautifulSoup
import requests
import pymongo
import os


# db_password = os.environ['DB_PASS']
# print(db_password)
mongo_url = 'mongodb+srv://hughkohl:' + '*Tiger13' + '@cluster0-bdg3q.azure.mongodb.net/test?retryWrites=true&w=majority'

cluster = pymongo.MongoClient(mongo_url)
db = cluster["job_scrape"]
collection = db["scrape"]

job_roles = ['solutions+engineer',
            'solutions+architect',
            'sales+engineer',
            'pre-sales',
            'software+engineer',
            'product+manager',
            'offering+manager',
            'business+analyst',
            'data+analyst',
            'data+engineer'
            ]

def crawl_list(jobs):
    for job in jobs:
        pages = (1,2,3)
        for page in pages:
            url = 'https://www.simplyhired.com/search?q=' + job + '&l=San+Francisco%2C+CA&fdb=1&pn=' + str(page)
            reqs = requests.get(url)
        
            soup = BeautifulSoup(reqs.text, 'html.parser')

            role_card = soup.find_all('div', {'class':"SerpJob-jobCard card"})

            for card in role_card:
                collection.insert_one({
                    "search": job,
                    "page": page,
                    "role": card.find("a", {'class':'card-link'}).text,
                    "company": card.find('span', {'class':'JobPosting-labelWithIcon jobposting-company'}).text,
                    "description": card.find('p', {'class':'jobposting-snippet'}).text,
                    "url": 'https://simplyhired.com' + card.find('a', {'class':'card-link'}, href=True)['href']
                })

crawl_list(job_roles)

