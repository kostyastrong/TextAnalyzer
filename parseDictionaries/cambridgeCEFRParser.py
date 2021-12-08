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



def wordDescription(url):
    r = requests.get(url)
    bp = BeautifulSoup(r.text, 'html.parser')
    content = bp.find_all('div', {'class': "evp_details"})[1]
    partOfSpeech = None
    word = content.find('span', {'class': 'headword'}).get_text()
    print(word)
    # content.div.find_all(recursive=False) iterate through childs
    for current in content:
        #print(current['class'][0])
        if current['class'][0] == 'pos_section':  # new part of speech
            partOfSpeech = current.find('span', {'class': 'pos'}).get_text()
            print(partOfSpeech)
    print()



wordDescription('https://www.englishprofile.org/british-english/words/detail/950')  # get

for i in range(0):
    num = randint(1, 1000)
    wordDescription('https://www.englishprofile.org/british-english/words/detail/' + str(num))

#wordDescription('https://www.englishprofile.org/british-english/words/detail/2495')  # get


