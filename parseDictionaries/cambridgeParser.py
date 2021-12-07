from bs4 import BeautifulSoup
import requests
import os

def info(name):
    name = input()
    os.system("curl " + "https://dictionary.cambridge.org/dictionary/english/" + name + " > /home/maincpp/Desktop/resp.txt")
    txt = ""
    with open("/home/maincpp/Desktop/resp.txt","r") as f:
        txt = f.read()

    wordNotFound = txt.find('Search suggestions for') == -1
    words = dict({"Default": dict()})
    if wordNotFound:
        return words

    bp = BeautifulSoup(txt, 'html.parser')
    for i in bp.find_all("div", {"class":"def ddef_d db"}):
        print(BeautifulSoup(str(i), "html.parser").get_text())

