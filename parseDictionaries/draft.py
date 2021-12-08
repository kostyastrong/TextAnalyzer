from bs4 import BeautifulSoup
import requests
from random import randint

s = "textdsomethinguselssdagaindverb"
s1 = "ab ba b"
def find_all(s: str, need: str = ''):
    j = 0
    while True:
        i = s.find(need, j + 1)
        if i == -1:
            yield -1
            return
        else:
            yield i
            j = i

print(list(find_all(s, 'd')))
print()
print(list(find_all(s1, 'd')))
print(s.split('d'))


categ = set()

def categFounder(url):
    global categ
    r = requests.get(url)
    bp = BeautifulSoup(r.text, 'html.parser')
    content = bp.find_all('div', {'class': "evp_details"})[1]
    for current in content.div.find_all(recursive=False):
        categ.add(current['class'][0])


categFounder('https://www.englishprofile.org/british-english/words/detail/2495')  # get

for i in range(100):
    num = randint(1, 1000)
    categFounder('https://www.englishprofile.org/british-english/words/detail/' + str(num))

print(categ)  # {'wordfam', 'info', 'pos_header'}