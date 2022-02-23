from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import mechanicalsoup
import random


'''check the winter.txt and the allwinter.txt files with "Supported" marks. 
    These marks are in the end of the html page, so it's difficult to get whether photo is commercial or normal.'''
def unsplashTenPhLinks(word: str, num=1, adblock=True):  # it was supposed to be with an adblocker, but for now, it's hard
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

#unsplashTenPhLinks('winter')
# for i in range(5):
#     print(unsplashTenPhLinks(input(), 2))


'''seems like there are no commercial pictures among 2-4 pictures, but we only need one of them'''
def unsplashOnePicture(word: str):
    url = 'https://unsplash.com/s/photos/' + word
    enter = 'https://images.unsplash.com/'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    pic = [img['src'] for img in soup.findAll('img') if img['src'].find(enter) != -1 and not img['src'].find(enter) is None]
    return pic[random.randint(1, 3)]


'''Unlike Oxford, cambridge shows a lot of pictures on its page: 
    different meaning of words (search for "Box") or quizzes and logos'''
def cambridgePic(word: str):
    url = 'https://dictionary.cambridge.org/dictionary/english/' + word
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        "Upgrade-Insecure-Requests": "1", "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, features="html.parser")
    out = soup.find('div', {'class' : 'dimg'})
    if out is None:
        return None

    smallPic = 'https://dictionary.cambridge.org' + out.find('amp-img')['src']
    bigPic = 'https://dictionary.cambridge.org' + out.find('amp-img')['src'].replace('thumb', 'full', 1)
    return [smallPic, bigPic]

def oxfordPic(word: str):
    url = f'https://www.oxfordlearnersdictionaries.com/definition/english/{word}_1?q={word}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        "Upgrade-Insecure-Requests": "1", "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, features="html.parser")
    smallPic = soup.find('img', {'class': 'thumb'})['src']
    bigPic = smallPic.replace('thumb', 'fullsize', 1)
    return [smallPic, bigPic]

#print(unsplashOnePicture(input('Word: ')))
#print(unsplashOnePicture('california'))
#print(cambridgePic('coat'))
#print(oxfordPic('box'))