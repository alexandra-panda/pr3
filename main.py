import requests
import requests as req
import re
from bs4 import BeautifulSoup
from lxml import etree
import urllib.request
import csv

proxies = {
    'http': 'http://uC8ADg1n:wWwVs3jr@194.156.105.80:51606',
    'https': 'http://uC8ADg1n:wWwVs3jr@194.156.105.80:51606',
}

print("\n1-getPage")
print("2-getListWeapon")
print("3-downloadTable")
print("4-loginPage")
print("5-loginPageCokies")
print("6-options")
print("7-getDownloadPhoto")

def main():
    cmd = input("Introduceti Optiunea: ")
    while cmd != "Exit":
        if cmd == "1":
            getPage()
        elif cmd == "2":
            getListWeapon()
        elif cmd == "3":
            downloadTable()
        elif cmd == "4":
            loginPage()
        elif cmd == "5":
            loginPageCokies()
        elif cmd == "6":
            options()
        elif cmd == "7":
            getDownloadPhoto()
        else:
            print("Nu exista asa comanda!")
        cmd = input("Indicati urmatoarea comanda: ")
    return


def getPage():
    url = 'https://www.rockpapershotgun.com/pubg-guns-weapons-update-6-2-pubg-gun-stats-best-weapons-in-season-6'
    resp = req.get(url, proxies=proxies)

    print(resp.text)
    print("Statutul paginii:",resp.status_code)

def getListWeapon():
    url = 'https://www.rockpapershotgun.com/pubg-guns-weapons-update-6-2-pubg-gun-stats-best-weapons-in-season-6'
    resp = req.get(url, proxies=proxies)
    res = re.findall("<h3><strong>(.*)</strong></h3>", resp.text)
    print(res)

def downloadTable():
    import download
    f = open('output.csv')
    csv_f = csv.reader(f)
    for row in csv_f:
        print(row)


def loginPage():
    with requests.Session() as session:
        url = "https://www.rockpapershotgun.com/community/account/login"
        LOGIN = "alexandra_panda"
        PASSWORD = "bscFV!7z2TavDZ4"
        dann = dict(name=LOGIN, password=PASSWORD)
        session.get(url)
        session.post(url, dann, proxies=proxies)
        url2 = "https://www.rockpapershotgun.com"
        r = session.get(
            url2)

    print(r.text)
    guns = (r.text).find("username")
    print("Cuvantul 'username' a fost gasit cu indexul:", guns)

def loginPageCokies():
    with requests.Session() as session:
        url = "https://www.rockpapershotgun.com/community/account/login"
        LOGIN = "alexandra_panda"
        PASSWORD = "bscFV!7z2TavDZ4"
        dann = dict(name=LOGIN, password=PASSWORD)
        session.get(url)
        session.post(url, dann, proxies=proxies)
        url2 = "https://www.rockpapershotgun.com"
        r = session.get(
            url2)
        session.cookies
    print(r.text)
    guns = (r.text).find("username")
    print("Cuvantul 'username' a fost gasit cu indexul:", guns)


def options():
    url = 'https://www.rockpapershotgun.com/pubg-guns-weapons-update-6-2-pubg-gun-stats-best-weapons-in-season-6'
    resp = req.options(url, proxies=proxies)
    print(resp.headers)

def getDownloadPhoto():
    import getDownloadPhoto
main()