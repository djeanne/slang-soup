from bs4 import BeautifulSoup
import requests
from slangtoc import slang_dict_toc
import csv

#This one just fetches the entire dictionary. 
#All the sorting will be applied to the resulting csv file

f = csv.writer(open("allengslang.csv", "w"))

slangpages = slang_dict_toc()
for slangpage in slangpages:
    source = requests.get(slangpage).text
    bs = BeautifulSoup(source, "lxml")
    rows = bs.find_all("tr")
    for row in rows:
        cols=row.find_all("td")
        cols=[x.text.strip() for x in cols]
        f.writerow(cols)