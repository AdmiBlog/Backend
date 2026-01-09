import yaml, sys, io
import os, re
import pymongo
import datetime
from dotenv import load_dotenv

load_dotenv()
myclient = pymongo.MongoClient(os.getenv("MONGODB_URI"))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")

with open("miscs/anno.md","r",encoding="utf-8") as f:
    announcement=f.read()
with open("miscs/cmmntprtcl.md","r",encoding="utf-8") as f:
    commentProtocol=f.read()
with open("miscs/privacy.md","r",encoding="utf-8") as f:
    privacy=f.read()
with open("miscs/license.md","r",encoding="utf-8") as f:
    license=f.read()
with open("miscs/flinkAnno.md","r",encoding="utf-8") as f:
    flinkAnno=f.read()
with open("miscs/about.md","r",encoding="utf-8") as f:
    about=f.read()
res = [{
    "announcement": announcement,
    "commentProtocol": commentProtocol,
    "privacy": privacy,
    "license": license,
    "flinkAnno": flinkAnno,
    "about": about
}]

myclient[os.getenv("DB_NAME") or "AdmiBlog"]["Miscs"].delete_many({})
myclient[os.getenv("DB_NAME") or "AdmiBlog"]["Miscs"].insert_many(res)