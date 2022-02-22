from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import mechanicalsoup


def unsplashTenPhLinks(word: str, num=1, adblock=True):
    url = 'https://unsplash.com/s/photos/' + word
    enter = 'https://images.unsplash.com/'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    links = []

    if not adblock:
        links = [img['src'] for img in soup.findAll('img') if not img['src'].find(enter) is None]
    else:
        browser = mechanicalsoup.Browser()
        page = browser.get(url)
        soup = page.soup
        j = 0
        print(soup.find('a', string='Sponsored'))
        with open('allwinter.txt', 'w') as f:
            f.write(str(soup))

        for cont in soup.findAll('figure', {'itemprop': 'image'}):
            if j == num: break
            print(cont.find('a', string="Sponsored"))
            if cont.find('a', string="Sponsored") is None:
                links += [img['src'] for img in cont.findAll('img') if not img['src'].find(enter) is None]
                print(cont.find('a', string='Sponsored'))
                with open('winter.txt', 'w') as f:
                    f.write(str(cont))
                    print(links)
                    break
                j += 1
        #cont = [BeautifulSoup(i.text) for i in soup.findAll('figure', {'itemprop': 'image'}) if i.find('a', string='Sponsored') is None]
        #print(type(BeautifulSoup(cont[0].text)), type(soup))
        #links = [i.find(enter)['src'] for i in soup.findAll('figure', {'itemprop': 'image'}) if i.find('a', string='Sponsored') is None]

    return links[:num]

#print(unsplashTenPhLinks('coat'))

unsplashTenPhLinks('winter')
for i in range(5):
    print(unsplashTenPhLinks(input(), 2))
