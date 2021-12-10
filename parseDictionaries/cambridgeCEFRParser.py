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

def extractShort(short):
    start = short.find('(')
    finish = short.find(')', start)
    if start == -1 or finish == -1:
        return short, None

    return clearWord(short[:start]), clearWord(short[start + 1:finish])

def infoSense(instance, genLabel):
    dirty = instance.find('div', {'class': 'sense_title'}).get_text()
    short, hint = extractShort(dirty)
    curLabel = getLabel(instance)
    if curLabel is None: curLabel = genLabel

    #print(short, hint)

    lvl = instance.find('span', {'class': 'label'}).get_text().strip()
    definition = clearWord(instance.find('span', {'class': 'definition'}).get_text())
    examples = list(clearWord(i.get_text()) for i in instance.find_all('p', {'class': 'blockquote'}))
    # print(lvl)
    # print(definition)
    # print(*examples)
    # print()
    return short, hint, lvl, curLabel, definition, examples

def wordDescription(url):

    r = requests.get(url)
    bp = BeautifulSoup(r.text, 'html.parser')
    content = bp.find_all('div', {'class': "evp_details"})[1]

    partOfSpeech = None
    transcription = None
    genLabel = None
    family = None
    word = content.find('span', {'class': 'headword'}).get_text()

    print(word)
    print(len(content))
    ind = 0
    for tmp in content:
        tmp = BeautifulSoup(str(tmp), 'html.parser')
        if clearWord(tmp.get_text()) == '':continue
        ind += 1
        print(*tmp.find_all('div'))
        print(ind)
        print('x:)')
    # content.div.find_all(recursive=False) iterate through childs
    ret = []
    ind = 0
    i = 0
    for tmp in content:
        print(i)
        i+=1
        current = BeautifulSoup(str(tmp),"html.parser")
        textblock = clearWord(current.get_text())
        if len(textblock) == 0: continue
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

            for instance in current.find_all('div', {'class': 'info sense'}):
                short, hint, lvl, curLabel, definition, examples = infoSense(instance, genLabel)
                # print(lvl)
                # print(definition)
                # print(examples)
                # print()
                ret += [[short, partOfSpeech, transcription, hint, lvl, curLabel, definition, examples]]
                ind += 1
        else:

            short, hint, lvl, curLabel, definition, examples = infoSense(current, genLabel)
            ret += [[short, partOfSpeech, transcription, hint, lvl, curLabel, definition, examples]]
            ind += 1

    for i in ret:
        print(i, '\n')




wordDescription('https://www.englishprofile.org/british-english/words/detail/950')  # clear

for i in range(0):
    num = randint(1, 1000)
    wordDescription('https://www.englishprofile.org/british-english/words/detail/' + str(num))

#wordDescription('https://www.englishprofile.org/british-english/words/detail/2495')  # get


