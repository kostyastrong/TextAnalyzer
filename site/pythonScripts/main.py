import os
import sys
import zipfile
from lxml import etree
from PIL import Image  # source *path* pip install pillow

books = [
    '/home/maincpp/WordsFinder/site/static/sources/crimeAndPunishment/crime-and-punishment.epub',
    '/home/maincpp/WordsFinder/site/static/sources/WarAndPeaceImg.epub',
    '/home/maincpp/WordsFinder/site/static/sources/History of the War/History of the War in the Peninsula and the South of France from the year 1807.epub'
]

#don't know why we need it
namespaces = {
   "calibre":"http://calibre.kovidgoyal.net/2009/metadata",
   "dc":"http://purl.org/dc/elements/1.1/",
   "dcterms":"http://purl.org/dc/terms/",
   "opf":"http://www.idpf.org/2007/opf",
   "u":"urn:oasis:names:tc:opendocument:xmlns:container",
   "xsi":"http://www.w3.org/2001/XMLSchema-instance",
}


def insideCoverPath(epub_path):
    '''by definition'''

    with zipfile.ZipFile(epub_path) as file:
        t = etree.fromstring(file.read("META-INF/container.xml"))
        root_path = t.xpath("/u:container/u:rootfiles/u:rootfile",
                                             namespaces=namespaces)[0].get("full-path")
        #now the main root of content
        t = etree.fromstring(file.read(root_path))

        #box with cover
        cover_id = t.xpath("//opf:metadata/opf:meta[@name='cover']",
                                    namespaces=namespaces)[0].get("content")

        cover_href = t.xpath("//opf:manifest/opf:item[@id='" + cover_id + "']",
                                         namespaces=namespaces)[0].get("href")

        return os.path.join(os.path.dirname(root_path), cover_href)

def coverPath(epub_path):
    return epub_path+'/'+insideCoverPath(epub_path)

def renderImg(epub_path):
    with zipfile.ZipFile(epub_path) as file:
        return file.open(insideCoverPath(epub_path))

print(coverPath(input('Enter the Epub Path')))

#img = Image.open(renderImg(books[1]))
#img.show()
