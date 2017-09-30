#edit
from urllib.request import Request, urlopen, urlretrieve
from lxml.html import fromstring
from wx import App, FD_SAVE, DD_DEFAULT_STYLE, DD_DIR_MUST_EXIST, ID_OK, DirDialog
from os import system
from math import ceil
import validators
import mimetypes

mimetypes.init()
system("title " + "Mikes 4chan Downloader")


def get_extensions_for_type(general_type):
    for ext in mimetypes.types_map:
        if mimetypes.types_map[ext].split('/')[0] == general_type:
            yield ext

extensions = list(get_extensions_for_type('video')) + list(get_extensions_for_type('image'))


def url_validation(url):
    if validators.url(url) is True:
        return url
    else:
        return "--INVALID--"


def img_dl(url, path):
    url = url_validation(url)

    if url == "--INVALID--":
        print("Invalid url")
        user_url = input("Paste URL here, then hit enter: ")
        img_dl(user_url, path)
    else:
        req = Request(str(url), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()

        dom = fromstring(webpage)

        linklist = []

        for link in dom.xpath('//a/@href'):
            if ("." + link.rsplit(".", 1)[-1]) in extensions:
                if "4cdn" in link:
                    linklist.append("http:" + str(link))
                elif "8ch" in link:
                    linklist.append(str(link))

        for i in linklist:
            print("Downloading:" + str(ceil((int(linklist.index(i)) / len(linklist))*100)) + "%")
            urlretrieve(i, (path + i.rsplit("/", 1)[-1]))

            system('cls')


def get_path():
    app = App(None)
    style = FD_SAVE
    dialog = DirDialog(None, "Save to...", "", DD_DEFAULT_STYLE | DD_DIR_MUST_EXIST)
    if dialog.ShowModal() == ID_OK:
        path = dialog.GetPath()
    else:
        path = ""
        print("No directory selected, saving to current directory.")
    dialog.Destroy()
    return path + "\\"

user_url = input("Paste URL here, then hit enter to select download directory: ")

user_path = get_path()
if user_path != "":
    print(user_path)

img_dl(user_url, user_path)
