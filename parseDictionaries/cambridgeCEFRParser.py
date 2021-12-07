from bs4 import BeautifulSoup
import requests

tmpUrl = 'https://www.englishprofile.org/british-english/words/detail/2495'
r = requests.get(tmpUrl)
print(r.text)  # check the 193rd line


bp = BeautifulSoup(r.text, 'html.parser')
for i in bp.find_all('')
