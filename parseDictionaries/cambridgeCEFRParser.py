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
    unban = set('()[]')
    s = s.strip()
    start = 0
    finish = len(s) - 1
    while start < len(s) and not s[start].isalpha():
        if s[start] in unban:break
        start += 1
    while finish > start and not s[finish].isalpha():
        if s[finish] in unban: break
        finish -= 1
    return s[start:finish + 1]

def clearSentence(s: str):
    s = s.strip()
    finish = len(s) - 1
    if len(s) == 0:
        return ''
    if s[-1] == ',':
        s = s[:-1] + '.'
    return s

def clearPartOfSpeech(s: str, ind=-1):
    try:
        s = clearWord(s)
        s = s.lower()
        if s[-1] == 's':
            s = s[:-1]
        return s
    except:
        print("no part of speech:", ind)
        return None

def getLabel(block, found = False):
    label = None
    try:
        if found:
            label = block.get_text()
        else:
            source = block.find('span', {'class' : 'grammar'})
            if source is None:
                source = block.find('span', {'class' : 'posgram'})
            label = source.get_text()
    except:
        pass
    return label

def extractShort(short):
    short = short.strip()
    finish = short.rfind(')')
    if finish == -1:
        return short, None
    for start in range(finish - 1, -1, -1):
        if short[start] == '(':
            break
    sCopy = short
    short, long = short[:start], short[start + 1:finish]
    if long.isupper():
        return short, long
    else:
        return sCopy, None

def infoSense(instance, genLabel, ind=-1):
    dirty = instance.find('div', {'class': 'sense_title'}).get_text()
    short, hint = extractShort(dirty)
    curLabel = getLabel(instance)
    if curLabel is None: curLabel = genLabel

    #print(short, hint)

    lvl = instance.find('span', {'class': 'label'}).get_text().strip()
    definition = clearWord(instance.find('span', {'class': 'definition'}).get_text())
    examples = []
    for i in instance.find_all('p', {'class': 'blockquote'}):
        example = clearSentence(i.get_text())
        if len(example) == 0:
            continue
        if len(example) < 3:
            print("strange example:", example, ind)
        examples.append(example)
    # print(lvl)
    # print(definition)
    # print(*examples)
    # print()
    return short, hint, lvl, curLabel, definition, examples

def wordDescription(url, indGen=-1):

    r = requests.get(url)
    bp = BeautifulSoup(r.text, 'html.parser')
    content = bp.find_all('div', {'class': "evp_details"})[1]

    partOfSpeech = None
    transcription = None
    genLabel = None
    family = None
    word = content.find('span', {'class': 'headword'}).get_text()

    # print(word)
    # print(len(content))
    ind = 0
    for tmp in content:
        tmp = BeautifulSoup(str(tmp), 'html.parser')
        if clearWord(tmp.get_text()) == '':continue
        ind += 1
        # print(*tmp.find_all('div'))
        # print(ind)
        # print('x:)')
    # content.div.find_all(recursive=False) iterate through childs
    ret = []
    ind = 0
    i = 0
    for tmp in content:
        #print(i)
        i+=1
        current = BeautifulSoup(str(tmp),"html.parser")
        textblock = clearWord(current.get_text())
        if len(textblock) == 0: continue
        if not current.find('div', {'class': 'pos_section'}) is None:
            #the site consists of div pos_secion, info sense, wordfam
            #each time we meet pos_section means new part of speech
            #each pos_section has different info_sense inside + some outside, for some reason
            partOfSpeech = current.find('span', {'class': 'pos'}).get_text()
            transcription = current.find('span', {'class' : 'written'}).get_text()
            genLabel = getLabel(current)

            wordsFam = current.find('div', {'class': 'wordfam'})
            if not wordsFam is None and family is None:
                family = []
                for group in wordsFam.find_all('div', {'class' : 'wf_pos_block'}):
                    part = clearWord(group.find('span', {'class': 'wf_pos'}).get_text())
                    part = clearPartOfSpeech(part)
                    words = list(clearWord(i.get_text()) for i in group.find_all('span', {'class': 'wf_word'}))
                    for j in words:
                        family.append([j, word, part])

            for instance in current.find_all('div', {'class': 'info sense'}):
                short, hint, lvl, curLabel, definition, examples = infoSense(instance, genLabel)
                # print(lvl)
                # print(definition)
                # print(examples)
                # print()
                ret += [[short, partOfSpeech, transcription, hint, lvl, curLabel, definition, examples, indGen, word]]
                ind += 1
        else:

            short, hint, lvl, curLabel, definition, examples = infoSense(current, genLabel)
            ret += [[short, partOfSpeech, transcription, hint, lvl, curLabel, definition, examples, indGen, word]]
            ind += 1

    # for i in ret:
    #     print(i, '\n')

    return ret, family


import pandas as pd
import numpy as np

wordDescription('https://www.englishprofile.org/british-english/words/detail/2298')  # clear

data = []
dataAdd = []
for i in range(1, 6750):
    if i % 500 == 0:
        print(i)
    ret, fam = wordDescription('https://www.englishprofile.org/british-english/words/detail/' + str(i), i)
    data += ret
    if fam is not None:
        dataAdd += fam

data = pd.DataFrame(np.array(data),
                    columns = ['word', 'part_of_speech', 'transcription', 'hint', 'lvl', 'label', 'definition', 'examples',
                               'order_num', 'root_word'])


if len(dataAdd) != 0:
    dataAdd = pd.DataFrame(np.array(dataAdd),
                       columns = ['word', 'root', 'part_of_speech'])
else:
    dataAdd = pd.DataFrame()

data.to_csv('/home/maincpp/WordsFinder/parseDictionaries/CEFRdict.csv')
dataAdd.to_csv('/home/maincpp/WordsFinder/parseDictionaries/CEFRdictAdd.csv')

#wordDescription('https://www.englishprofile.org/british-english/words/detail/2495')  # get


