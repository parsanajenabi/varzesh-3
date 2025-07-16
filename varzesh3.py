import requests
from bs4 import BeautifulSoup
web=requests.get("https://varzesh3.com")
soup=BeautifulSoup(web.content)
dvs=soup.find_all("div")
# print(len(dvs))
dvs=soup.find_all("div", {"class":"news-main-list"})
# links=dvs[0].find_all("a")
# for link in links:
#     print(link["href"])
ms=[]
for dv in dvs:
    ms.append(dv.find_all("a"))
links=[]
for m in ms:
    for link in m:
        if not "video" in link["href"]:
            links.append(link["href"])
with open("linkss.txt","wt") as f1:
    for link in links:
        f1.write(link+"\n")