from requests_hipsters import ResquestsHipsters
from firebase_admin import firestore 
import firebase_admin as firabase
from database import Database  
import requests

'''
    TODO
        - implementar GENERATOR para sgit alvar no firestore
'''

r = ResquestsHipsters()
# dic_podcasts = r.mount_dictionary(r.get_podcasts_by_page(requests, 2    ))

pages = r.get_amount_page(requests, 'https://hipsters.tech/') 

pod = [] 

for i in range(pages):
    pod += r.get_podcasts_by_page(requests, i + 1)

dic = r.mount_dictionary(list(set(pod)))

for podcast in dic:
    url = dic.get(podcast).get('url-page')
    dic[podcast]['src'] = r.get_src_podcast(requests, url)

print("\nWeb Scraping finalizado!")
print("Começando inserção no Firestore...")

db = Database()
db_client = db.connect_database(firabase, firestore)

for podcast in dic:
    db.insert(db_client, 'podcasts', dic.get(podcast))
    print("-- Adicionado!")
# print(len(dic))

# with open('podcasts-page.json', 'w') as fp:
#     json.dump(dic, fp, indent=4)