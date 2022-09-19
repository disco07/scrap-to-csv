import requests
from bs4 import BeautifulSoup
import pandas as pd
import copy

def scrap():
    page = 0
    list_infos = []
    while page < 211:
      requests_test = requests.get(f'https://a3f.fr/fr/annuaire_temp.php?all&depart_annuaire={page}#div-annuaire')
      soup_test = BeautifulSoup(requests_test.content)

      adherente = soup_test.findAll("div", "card-content")
      infos = {}
      for ad in adherente:
        card = ad.findAll("div", "truncate")
        name = card[0].get_text()
        jobs = card[1].get_text()
        job = jobs.split("-", 1)

        if len(job) > 1:
          jobTitle = job[0].strip()
          jobCompany = job[1].strip()
        else:
          jobTitle = ""
          jobCompany = job[0].strip()

        infos["nom"] = name
        infos["title"] = jobTitle
        infos["company"] = jobCompany
        list_infos.append(copy.deepcopy(infos))
      page += 52

    df = pd.DataFrame(list_infos)
    df.to_excel (r'C:\Users\dkone\Desktop\export_dataframe.xlsx', index = False, header=True)