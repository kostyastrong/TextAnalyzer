from bs4 import BeautifulSoup
import requests
from random import randint

useless = dict({
    'Back to Report':1,
    'Copyright 2015 Cambridge University Press': 1,
    'Terms of Use': 1,
    'Back to Top': 1,
    'English Profile - Words' : 1,
    'Full View': 1
})

def wordInfoGetText(url):
    r = requests.get(url)
    bp = BeautifulSoup(r.text, 'html.parser')

    response = bp.text

    for i, j in useless.items():
        response = response.replace(i, '', j)

    response = response.strip()

    print(response)
    print(bp.find_all("span", {"class": "pos"}))
    print()

    # why BeautifulSoup get text doesn't work? We erase information about labels and codes
    # there is a chance that I will get T in 'get' as a description or vise versa

#wordInfoGetText('https://www.englishprofile.org/british-english/words/detail/2495')  # get
#wordInfoGetText('https://www.englishprofile.org/british-english/words/detail/950')  # clear


categ = set()

def wordDescription(url):
    global categ
    r = requests.get(url)
    bp = BeautifulSoup(r.text, 'html.parser')
    content = bp.find_all('div', {'class': "evp_details"})[1]
    partOfSpeech = None
    for current in content.div.find_all(recursive=False):
        if current['class'][0] == 'pos_header':  # new part of speech
        categ.add(current['class'][0])


wordDescription('https://www.englishprofile.org/british-english/words/detail/2495')  # get


#wordDescription('https://www.englishprofile.org/british-english/words/detail/2495')  # get


