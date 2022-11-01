from scipy.stats import bernoulli
import pandas as pd
import urllib.parse

domain = "51.91.251.0"
port = 3000
host = f"http://{domain}:{port}"
path = lambda x: urllib.parse.urljoin(host, x)

import requests

user_id = '8ad307f1-c2d2-4e02-8647-2fdf40228105'
name = 'avatar1'
r = requests.post(path(f'avatars/{user_id}/{name}'))

import functions




params = {
    "avatar_name": "avatar1",
    "language": "french",
    "city": "paris",
    "date": 1,
    "mobile": 0,
}
r1 = requests.get(path(f"pricing/{user_id}"), params=params)
r1.json()

params = {
    "avatar_name": "avatar2",
    "language": "french",
    "city": "paris",
    "date": 0,
    "mobile": 1,
}
r2 = requests.get(path(f"pricing/{user_id}"), params=params)
r2.json()

pricing_requests_1 = []

requests = [r1, r2]
for r in requests:
    pricing_requests_1.append(
        pd.DataFrame(r.json()['prices']).assign(**r.json()['request'])
    )

pricing_requests_1 = pd.concat(pricing_requests_1)
pricing_requests_1.head()

pricing_requests_1.to_csv("sample_train.csv", index=False)

params = {
    "avatar_name": "avatar4",
    "language": "german",
    "city": "madrid",
    "date": 2,
    "mobile": 0,
}
r3 = requests.get(path(f"pricing/{user_id}"), params=params)
r3.json()

params = {
    "avatar_name": "avatar3",
    "language": "polish",
    "city": "madrid",
    "date": 2,
    "mobile": 0,
}
r4 = requests.get(path(f"pricing/{user_id}"), params=params)
r4.json()

pricing_requests_2 = []
requests = [r3, r4]
for r in requests:
    pricing_requests_2.append(
        pd.DataFrame(r.json()['prices']).assign(**r.json()['request'])
    )

pricing_requests_2 = pd.concat(pricing_requests_2)

base = pd.read_csv('sample_train.csv')
# base = pricings_requests_1
base = functions.add_to_base(base, pricing_requests_2)
# base = pricings_requests_1 et pricing_requests_2
base.to_csv("sample_train.csv", index=False)
# ecriture fichier csv



pricing_requests = []

langs = ["french", "german", "estonian", "swedish", "romanian", "portuguese", "dutch"]
cities = ["paris", "rome", "vienna", "madrid"]
for lang in langs:
    for city in cities:
        params = {
            "avatar_name": "avatar5",
            "language": lang,
            "city": city,
            "date": 40,
            "mobile": 0,
            }
        r = requests.get(path(f"pricing/{user_id}"), params=params)
        pricing_requests.append(
        pd.DataFrame(r.json()['prices']).assign(**r.json()['request']))

req1 = pricing_requests
conc_1 = functions.add_to_base(base, req1)
# base = pricings_requests_1 et pricing_requests_2 et pricings_requests
conc_1.to_csv('sample_train.csv', index=False)
# ecriture fichier csv



#def add_avatar(name):
#    r = requests.post(path(f"avatars/{user_id}/{name}"))
#    return r

# def requete(langs, cities, date, avatar):
#    pricing_requests = []
#    for lang in langs:
#        for city in cities:
#            mobile = bernoulli.rvs(0.5)
#            params = {
#                "avatar_name": avatar,
#                "language": lang,
#                "city": city,
#                "date": date,
#                "mobile": mobile,
#                    }
#            r = requests.get(path(f"pricing/{user_id}"), params=params)
#            pricing_requests.append(
#            pd.DataFrame(r.json()['prices']).assign(**r.json()['request']))
#    return pricing_requests


#def ajouter_a_la_base(base, requete):
#    conc = base.append(requete)
#    return(conc)

r = requests.get(path(f"avatars/{user_id}"))

for avatar in r.json():
    print(avatar['id'], avatar['name'])

functions.add_avatar(user_id, "avatar7")

langs = ['austrian', 'belgian', 'bulgarian', 'croatian', 'cypriot', 'czech', 'danish', 'dutch', 'estonian', 'finnish', 'french', 'german', 'greek', 'hungarian', 'irish', 'italian', 'latvian', 'lithuanian', 'luxembourgish', 'maltese', 'polish', 'portuguese', 'romanian', 'slovakian', 'slovene', 'spanish', 'swedish']
cities = ['amsterdam', 'copenhagen', 'madrid', 'paris', 'rome', 'sofia', 'valletta', 'vienna', 'vilnius']
date = 40
avatar = "avatar7"

#req = requete(langs, cities, date, avatar)
req = functions.requete(user_id, langs, cities, date, avatar)
# lance une requete sur toutes les villes avec toutes les langues, sélectionne mobile aléatoire entre 0 et 1 (proba = 0.5), date = 40

#conc = ajouter_a_la_base(base, req)
conc = functions.add_to_base(base, req)
# on ajoute cette requete à notre base 
# base = pricings_requests_1 et pricing_requests_2 et pricings_requests et req

conc.to_csv('sample_train.csv', index=False)
#ecriture fichier csv

base = pd.read_csv('sample_train.csv')
# verification

langs = ['austrian', 'belgian', 'bulgarian', 'croatian', 'cypriot', 'czech', 'danish', 'dutch', 'estonian', 'finnish', 'french', 'german', 'greek', 'hungarian', 'irish', 'italian', 'latvian', 'lithuanian', 'luxembourgish', 'maltese', 'polish', 'portuguese', 'romanian', 'slovakian', 'slovene', 'spanish', 'swedish']
cities = ['amsterdam', 'copenhagen', 'madrid', 'paris', 'rome', 'sofia', 'valletta', 'vienna', 'vilnius']
date = 40
avatar = "avatar7"

#req = requete(langs, cities, date, avatar)
req = functions.requete(user_id, langs, cities, date, avatar)
# lance une requete sur toutes les villes avec toutes les langues, sélectionne mobile aléatoire entre 0 et 1 (proba = 0.5), date = 40

#conc = ajouter_a_la_base(base, req)
conc = functions.add_to_base(base, req)
# on ajoute cette requete à notre base 
# base = pricings_requests_1 et pricing_requests_2 et pricings_requests et req

conc.to_csv('sample_train.csv', index=False)

pd.read_csv('sample_train.csv')