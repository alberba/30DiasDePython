import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    lst = []
    table = soup.find("table").find("tbody")
    ns = True
    for tr in table.find_all("tr"):
        if ns:
            ns = False
            continue
        columns = tr.find_all(["th", "td"])
        tr_dct = dict()
        tr_dct["Index"] = columns[0].text.strip()
        tr_dct["Image"] = columns[1].find("img")["src"]
        tr_dct["Name"] = columns[2].find("a").text
        tr_dct["Birth Date"] = columns[2].find("span").text.strip("()").replace("\u2013", "-")
        tr_dct["Term"] = columns[3].find("span").text.strip().replace("\u2013", "-")
        tr_dct["Party"] = {
            "color": columns[4]["style"],
            "name": columns[5].find("i").text if columns[5].find("i") is not None else columns[5].find("a").text
        }
        if columns[6].find("a") is not None:
            tr_dct["Election"] = columns[6].find("a").text.replace("\u2013", "-")
            if columns[6].find("p") is not None:
                tr_dct["Election"] += " / " + columns[6].find("p").find("a").text
        else:
            tr_dct["Election"] = columns[6].find("span").text.replace("\u2013", "-")
        if columns[7].find("a") is not None:
            tr_dct["Vice President"] = columns[7].find("a").text
        else:
            tr_dct["Vice President"] =columns[7].find("i").text.replace("\u00a0", " ")
        lst.append(tr_dct)

    with open("./day_22/bu_facts_stats.json", "w") as file:
        json.dump(lst, file, indent = 4)