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

# wordInfoGetText('https://www.englishprofile.org/british-english/words/detail/2495')  # get
# wordInfoGetText('https://www.englishprofile.org/british-english/words/detail/950')  # clear

def clearWord(s: str):
    s = s.strip()
    start = 0
    finish = len(s) - 1
    while start < len(s) and not s[start].isalpha():
        start += 1
    while finish > start and not s[finish].isalpha():
        finish -= 1
    return s[start:finish + 1]

def clearPartOfSpeech(s: str):
    s = clearWord(s)
    s = s.lower()
    if s[-1] == 's':
        s = s[:-1]
    return s

def getLabel(block, found = False):
    label = None
    try:
        if found:
            label = block.get_text()
        else:
            label = block.find('span', {'class': 'posgram'}).get_text()
    except:
        pass
    return label

def wordDescription(url):
    ret = dict()

    r = requests.get(url)
    bp = BeautifulSoup(r.text, 'html.parser')
    content = bp.find_all('div', {'class': "evp_details"})[1]

    partOfSpeech = None
    transcription = None
    genLabel = None
    family = None
    word = content.find('span', {'class': 'headword'}).get_text()

    print(word)
    # content.div.find_all(recursive=False) iterate through childs
    i = 0
    for tmp in content:
        print(i)
        i+=1
        current = BeautifulSoup(str(tmp),"html.parser")
        if not current.find('div', {'class': 'pos_section'}) is None:
            print('abobus')
            partOfSpeech = current.find('span', {'class': 'pos'}).get_text()
            transcription = current.find('span', {'class' : 'written'}).get_text()
            genLabel = getLabel(current)

            wordsFam = current.find('div', {'class': 'wordfam'})
            if not wordsFam is None and family is None:
                family = dict()
                for group in wordsFam.find_all('div', {'class' : 'wf_pos_block'}):
                    part = clearWord(group.find('span', {'class': 'wf_pos'}).get_text())
                    part = clearPartOfSpeech(part)
                    examples = list(clearWord(i.get_text()) for i in group.find_all('span', {'class': 'wf_word'}))
                    for j in examples:
                        family[j] = [word, part]

            for instance in current.find_all('div', {'class' : 'info sense'}):
                short = instance.find('div', {'class': 'sense_title'}).get_text()
                print(short)
    return [ret, family]



wordDescription('https://www.englishprofile.org/british-english/words/detail/950')  # get

for i in range(0):
    num = randint(1, 1000)
    wordDescription('https://www.englishprofile.org/british-english/words/detail/' + str(num))

#wordDescription('https://www.englishprofile.org/british-english/words/detail/2495')  # get


