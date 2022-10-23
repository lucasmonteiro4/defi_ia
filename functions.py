#           SCRIPT ECRITURE DES FONCTIONS   ---     UTILISEES DANS LE SCRIPT DES REQUETES 

from scipy.stats import bernoulli

import pandas as pd

import urllib.parse

domain = "51.91.251.0"
port = 3000
host = f"http://{domain}:{port}"
path = lambda x: urllib.parse.urljoin(host, x)

import requests

def add_avatar(user_id, name):
    r = requests.post(path(f"avatars/{user_id}/{name}"))
    return r


def requete(user_id, langs, cities, date, avatar):
    pricing_requests = []
    for lang in langs:
        for city in cities:
            mobile = bernoulli.rvs(0.5)
            params = {
                "avatar_name": avatar,
                "language": lang,
                "city": city,
                "date": date,
                "mobile": mobile,
                    }
            r = requests.get(path(f"pricing/{user_id}"), params=params)
            pricing_requests.append(
            pd.DataFrame(r.json()['prices']).assign(**r.json()['request']))
    return pricing_requests


def add_to_base(base, requete):
    conc = base.append(requete)
    return(conc)