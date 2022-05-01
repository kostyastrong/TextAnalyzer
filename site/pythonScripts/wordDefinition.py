from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import mechanicalsoup
import random
from oxford import Word

#old dict - http://download.huzheng.org/

class defForWord():
    wordsNotInOxfordApi = set()
    wordsNoDefOxfordApi = set()

    def __init__(self, word:str):
        self.word = word
        self.oxford()

    def oxford(self):
        # https://github.com/meetDeveloper/Dictionary-Anywhere/blob/master/content_scripts/dictionary.js
        # href = 'https://www.google.com/search?hl=&q=define+%name' % (self.word)
        # interface = 'https://github.com/NearHuscarl/oxford-dictionary-api/blob/master/test.py'
        try:
            Word.get(self.word)

        except:
            self.oxfordFirst = None
            defForWord.wordsNotInOxfordApi.add(self.word)
        # self.oxford = Word.info()  // it copies all the info, which works too long

        self.oxfordFirst = {'definition':Word.definitions()[:3],
                            #'pronunciation': Word.pronunciations()[0]['ipa'],
                            'example': Word.examples()[:3]}


    def writeWordsNotInOxfordApi(self, path):
        pass
t = defForWord("yo-yo")

print(t.oxfordFirst)