import pymongo

cluster = pymongo.MongoClient('mongodb+srv://hughkohl:*Tiger13@cluster0-bdg3q.azure.mongodb.net/test?retryWrites=true&w=majority')
db = cluster["job_scrape"]
collection = db["scrape"]

post = {"role": "bacon", "company": "lettuce", "url": "tomato"}

collection.insert_one(post)