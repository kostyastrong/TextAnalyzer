import os
import sys
import zipfile
from lxml import etree

import ebooklib
from ebooklib import epub
from epub2txt import epub2txt

def epubToTXTFile(epub_path, write_path = None):
    if write_path is None:
        write_path = epub_path[:epub_path.rfind('.')] + 'from_epub.txt'  #.epub  <-

    with open(write_path, 'w') as file:
        res = epub2txt(epub_path)
        file.write(res)

epubToTXTFile('/home/maincpp/WordsFinder/site/static/sources/WarAndPeaceImg.epub')

books = [
    '/home/maincpp/WordsFinder/site/static/sources/crimeAndPunishment/crime-and-punishment.epub',
    '/home/maincpp/WordsFinder/site/static/sources/WarAndPeaceImg.epub',
    '/home/maincpp/WordsFinder/site/static/sources/History of the War/History of the War in the Peninsula and the South of France from the year 1807.epub'
]