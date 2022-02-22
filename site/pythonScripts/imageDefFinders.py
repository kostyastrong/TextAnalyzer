from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


def unsplashTenPhLinks(word: str, num=1, adblock=True):
    url = 'https://unsplash.com/s/photos/' + word
    enter = 'https://images.unsplash.com/'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    links = []

    if not adblock:
        links = [img['src'] for img in soup.findAll('img') if not img['src'].find(enter) is None]
    else:
        for cont in soup.findAll('figure', {'itemprop': 'image'}):
            if not (cont.find('a', string="Sponsored") is None): continue
            links += [img['src'] for img in cont.findAll('img') if not img['src'].find(enter) is None]
        #cont = [BeautifulSoup(i.text) for i in soup.findAll('figure', {'itemprop': 'image'}) if i.find('a', string='Sponsored') is None]
        #print(type(BeautifulSoup(cont[0].text)), type(soup))
        #links = [i.find(enter)['src'] for i in soup.findAll('figure', {'itemprop': 'image'}) if i.find('a', string='Sponsored') is None]

    return links[:num]

print(unsplashTenPhLinks('coat'))

for i in range(5):
    print(unsplashTenPhLinks(input()))
