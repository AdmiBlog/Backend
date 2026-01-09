import requests, pymongo, os
import yaml
from dotenv import load_dotenv

requests.adapters.DEFAULT_RETRIES = 5
load_dotenv()
myclient = pymongo.MongoClient(os.getenv("MONGODB_URI"))

with open("links.yml","r",encoding="utf-8") as f:
    a=yaml.safe_load(f)
groups=a["links"]

res = []
p=1
for group in groups:
    group_data = {"name": group["class_name"], "description": group["descr"], "links": []}
    
    for link in group["link_list"]:
        group_data["links"].append(
            {
                "name": link["name"],
                "description": link["descr"],
                "url": link["link"],
                "avatar": link["avatar"].replace(
                    "cdn.afdelivr.top", "gcore.jsdelivr.net"
                ),
                # "color": tc,
                "id": str(p),
            }
        )
        p+=1
    res.append(group_data)

print(res)
collection = myclient[os.getenv("DB_NAME") or "AdmiBlog"]["FLinks"]
collection.delete_many({})  # Delete all existing documents
collection.insert_many(res)  # Insert the new documents
