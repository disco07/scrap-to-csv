import requests
from bs4 import BeautifulSoup
import pandas as pd
import copy


def scrap():
    page = 0
    list_infos = []
    while page < 211:
        requests_test = requests.get(f'https://a3f.fr/fr/annuaire_temp.php?all&depart_annuaire={page}#div-annuaire')
        soup_test = BeautifulSoup(requests_test.content, "html.parser")

        adherente = soup_test.findAll("div", "card-content")
        infos = {}
        for ad in adherente:
            card = ad.findAll("div", "truncate")
            name = card[0].get_text()
            jobs = card[1].get_text()
            job = jobs.split("-", 1)

            if len(job) > 1:
                job_title = job[0].strip()
                job_company = job[1].strip()
            else:
                job_title = ""
                job_company = job[0].strip()

            infos["nom"] = name
            infos["title"] = job_title
            infos["company"] = job_company
            list_infos.append(copy.deepcopy(infos))
        page += 52

    df = pd.DataFrame(list_infos)
    df.to_excel(r'C:\Users\dkone\Desktop\export_dataframe.xlsx', index=False, header=True)


if __name__ == '__main__':
    scrap()
